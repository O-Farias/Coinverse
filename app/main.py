from app.converter import convert_currency
from app.database import save_conversion, get_conversion_history
from colorama import Fore, Style
import os

def clear_console():
    """Limpa o terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def print_title(title):
    """Exibe um título estilizado."""
    print(Fore.CYAN + "=" * 30)
    print(f"{title.center(30)}")
    print("=" * 30 + Style.RESET_ALL)

def main_menu():
    """Menu principal."""
    while True:
        clear_console()
        print_title("💱 Conversor de Moedas 💱")
        print(Fore.GREEN + "1. Converter Moedas")
        print("2. Ver Histórico de Conversões")
        print("3. Sair" + Style.RESET_ALL)
        print(Fore.CYAN + "-" * 30 + Style.RESET_ALL)
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            handle_conversion()
        elif option == "2":
            show_history()
        elif option == "3":
            print(Fore.YELLOW + "\nObrigado por usar o Conversor de Moedas! 🙌" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\n❌ Opção inválida. Tente novamente." + Style.RESET_ALL)
            input("\nPressione ENTER para continuar...")

def handle_conversion():
    """Gerencia o processo de conversão de moedas."""
    clear_console()
    print_title("🌍 Conversão de Moedas 🌍")
    from_currency = input(Fore.CYAN + "Digite a moeda de origem (ex.: USD): " + Style.RESET_ALL).strip().upper()
    to_currency = input(Fore.CYAN + "Digite a moeda de destino (ex.: BRL): " + Style.RESET_ALL).strip().upper()
    amount = float(input(Fore.CYAN + "Digite o valor a ser convertido: " + Style.RESET_ALL).strip())

    try:
        result, rate = convert_currency(from_currency, to_currency, amount)
        print(Fore.GREEN + f"\n✅ {amount} {from_currency} = {result:.2f} {to_currency} (Taxa: {rate})" + Style.RESET_ALL)
        save_conversion(from_currency, to_currency, amount, result, rate)
    except Exception as e:
        print(Fore.RED + f"\n❌ Erro na conversão: {e}" + Style.RESET_ALL)
    
    input("\nPressione ENTER para voltar ao menu...")

def show_history():
    """Exibe o histórico de conversões."""
    clear_console()
    print_title("📜 Histórico de Conversões 📜")
    history = get_conversion_history()

    if not history:
        print(Fore.YELLOW + "\nNenhuma conversão registrada ainda." + Style.RESET_ALL)
    else:
        for record in history:
            print(Fore.CYAN + f"- {record['date']}: {record['amount']} {record['from']} → {record['to']} = {record['result']:.2f} (Taxa: {record['rate']})" + Style.RESET_ALL)

    input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    main_menu()
