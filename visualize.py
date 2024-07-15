import matplotlib.pyplot as plt
import datetime

# Utiliser le backend non interactif Agg
plt.switch_backend('Agg')

def read_log(file_path):
    dates = []
    temperatures = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            date_str, temp = line.strip().split(': ')
            dates.append(datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f'))
            temperatures.append(float(temp))
    return dates, temperatures

def plot_data(dates, temperatures):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='b')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Over Time')
    plt.grid(True)

    # Sauvegarder le graphique dans un fichier
    plt.savefig('temperature_plot.png')

if __name__ == '__main__':
    log_file_path = 'temperature_log.txt'
    dates, temps = read_log(log_file_path)
    plot_data(dates, temps)

