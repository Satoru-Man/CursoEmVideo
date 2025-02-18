from datetime import datetime, time, timedelta
import calendar

# Cores ANSI
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
AZUL = '\033[94m'
RESET = '\033[0m'

class AgendaMensal:
    def __init__(self, mes, ano):
        self.mes = mes
        self.ano = ano
        self.agenda = {}
        self.cal = calendar.Calendar(firstweekday=calendar.SUNDAY)  # Pode usar MONDAY se preferir
        # Inicializa todos os dias do mês com valores default
        _, ultimo_dia = calendar.monthrange(ano, mes)
        for dia in range(1, ultimo_dia + 1):
            self.agenda[dia] = {
                'entrada': '08:30',  # Novo default
                'saida': '17:30',    # Novo default
                'pausa_almoco': '30' # 30 minutos default
            }
    
    def get_semana_info(self, dia):
        """Retorna informações sobre a semana do mês e do ano"""
        data = datetime(self.ano, self.mes, dia)
        # Obtém as semanas do mês atual
        semanas_mes = list(self.cal.monthdatescalendar(self.ano, self.mes))
        
        # Encontra em qual semana o dia está
        for i, semana in enumerate(semanas_mes, 1):
            if data.date() in semana:
                semana_mes = i
                break
        
        semana_ano = data.isocalendar()[1]
        return semana_mes, semana_ano
    
    def converter_para_minutos(self, horas_str):
        """Converte string HH:MM para minutos"""
        horas, minutos = map(int, horas_str.split(':'))
        return horas * 60 + minutos
    
    def converter_para_horas(self, minutos):
        """Converte minutos para string HH:MM"""
        horas = minutos // 60
        mins = minutos % 60
        return f"{horas:02d}:{mins:02d}"
    
    def mostrar_mes_completo(self):
        """Mostra a matriz completa do mês"""
        print(f"\nAgenda - {calendar.month_name[self.mes]} {self.ano}")
        print("=" * 95)
        print(f"{'Dia':^6} | {'SM':^4} | {'SA':^4} | {'Entrada':^10} | {'Saída':^10} | {'Almoço':^12} | {'Horas Trab.':^12}")
        print("=" * 95)
        
        semana_mes_atual = 0
        total_minutos_semana = 0
        total_minutos_mes = 0
        
        dias_ordenados = sorted(self.agenda.keys())
        ultima_linha = None  # Variável para guardar a última linha
        
        for i, dia in enumerate(dias_ordenados):
            semana_mes, semana_ano = self.get_semana_info(dia)
            
            entrada = self.agenda[dia]['entrada']
            saida = self.agenda[dia]['saida']
            pausa = f"0:{self.agenda[dia]['pausa_almoco']}"
            horas = self.calcular_horas_trabalhadas(dia)
            
            # Adiciona ao total
            total_minutos_semana += self.converter_para_minutos(horas)
            total_minutos_mes += self.converter_para_minutos(horas)
            
            # Adiciona dia da semana
            data = datetime(self.ano, self.mes, dia)
            dia_semana = calendar.day_abbr[data.weekday()]
            
            # Verifica se é o último dia da semana atual ou último dia do mês
            proximo_dia = dias_ordenados[i + 1] if i + 1 < len(dias_ordenados) else None
            proxima_semana = self.get_semana_info(proximo_dia)[0] if proximo_dia else None
            eh_ultimo_da_semana = proxima_semana != semana_mes if proxima_semana else True
            
            # Prepara a linha base
            if data.weekday() == 6:  # Domingo
                linha = f"{VERMELHO}{dia:>2} {dia_semana:<3} | {semana_mes:^4} | {semana_ano:^4} | {entrada:^10} | {saida:^10} | {pausa:^12} | {horas:^12}{RESET}"
            elif data.weekday() == 5:  # Sábado
                linha = f"{AMARELO}{dia:>2} {dia_semana:<3} | {semana_mes:^4} | {semana_ano:^4} | {entrada:^10} | {saida:^10} | {pausa:^12} | {horas:^12}{RESET}"
            else:
                linha = f"{dia:>2} {dia_semana:<3} | {semana_mes:^4} | {semana_ano:^4} | {entrada:^10} | {saida:^10} | {pausa:^12} | {horas:^12}"
            
            # Adiciona subtotal se for último dia da semana
            if eh_ultimo_da_semana:
                subtotal = self.converter_para_horas(total_minutos_semana)
                linha = linha + f"{' ':>{70-66}}{AZUL}[{subtotal}] Σ Semana{RESET}"
                total_minutos_semana = 0
                if proximo_dia:  # Se não for o último dia do mês
                    print(linha)
                    print("-" * 95)
                else:  # Se for o último dia do mês
                    ultima_linha = linha  # Guarda a última linha para imprimir depois
            else:
                print(linha)
            
            if semana_mes != semana_mes_atual:
                semana_mes_atual = semana_mes
        
        # Imprime a última linha com seu subtotal
        if ultima_linha:
            print(ultima_linha)
        
        # Imprime total do mês
        print("=" * 95)
        total = self.converter_para_horas(total_minutos_mes)
        print(f"{' ':>{79}}{AZUL}[{total}] Σ Mês{RESET}")
    
    def editar_horario(self, dia, entrada=None, saida=None, pausa_almoco=None):
        """Edita os horários de um dia"""
        if dia in self.agenda:
            if entrada:
                self.agenda[dia]['entrada'] = entrada
            if saida:
                self.agenda[dia]['saida'] = saida
            if pausa_almoco:
                # Remove o '0:' se o usuário inserir nesse formato
                pausa_almoco = pausa_almoco.replace('0:', '') if ':' in pausa_almoco else pausa_almoco
                self.agenda[dia]['pausa_almoco'] = pausa_almoco
            return True
        return False
    
    def consultar_dia(self, dia):
        """Consulta os horários de um dia específico"""
        if dia in self.agenda:
            horarios = self.agenda[dia]
            return {
                'entrada': horarios['entrada'],
                'saida': horarios['saida'],
                'almoço': f"0:{horarios['pausa_almoco']}",
                'horas_trabalhadas': self.calcular_horas_trabalhadas(dia)
            }
        return "Dia não encontrado"
    
    def calcular_horas_trabalhadas(self, dia):
        """Calcula total de horas trabalhadas em um dia no formato HH:MM"""
        if dia in self.agenda:
            entrada = datetime.strptime(self.agenda[dia]['entrada'], '%H:%M')
            saida = datetime.strptime(self.agenda[dia]['saida'], '%H:%M')
            pausa = int(self.agenda[dia]['pausa_almoco'])
            
            # Calcula a diferença em minutos
            delta = saida - entrada
            minutos_totais = int(delta.total_seconds() / 60)  # converte para minutos
            minutos_totais -= pausa  # subtrai a pausa do almoço
            
            # Converte para formato HH:MM
            horas = minutos_totais // 60
            minutos = minutos_totais % 60
            
            return f"{horas:02d}:{minutos:02d}"
        return "00:00"

# Exemplo de uso:
if __name__ == "__main__":
    # Criar agenda para Fevereiro 2025
    agenda = AgendaMensal(mes=2, ano=2025)
    
    # Mostrar a matriz completa com valores default
    agenda.mostrar_mes_completo()
    
    # Exemplo de consulta
    print(f"\nConsulta dia 15:", agenda.consultar_dia(15)) 