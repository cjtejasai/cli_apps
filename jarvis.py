import click
import psutil
import platform


@click.command()
@click.argument('subcommand', type=click.Choice(['os', 'ram', 'cpu', 'disk', 'processes', 'ports']))
def jarvis(subcommand):
    try:
        if subcommand == 'os':
            click.echo(get_os_config())
        elif subcommand == 'ram':
            click.echo(get_ram())
        elif subcommand == 'cpu':
            click.echo(get_cpu_info())
        elif subcommand == 'disk':
            click.echo(get_disk_info())
        elif subcommand == 'processes':
            click.echo(get_processes())
        elif subcommand == 'ports':
            click.echo(get_ports())
    except Exception as e:
        click.echo(f"An error occurred: {e}")


def get_os_config():
    try:
        release_version = platform.release()
        os_version = platform.system() + ' ' + release_version
        os_info = f"💻 The operating system is the foundation of the computer. Without it, the computer is nothing. " \
                  f"💻\n\nRelease version: {release_version}\nOS version: {os_version} "
        return os_info
    except Exception as e:
        return f"An error occurred: {e}"


def get_ram():
    try:

        ram_info = psutil.virtual_memory()
        total_ram = ram_info.total / (1024 ** 3)
        used_ram = ram_info.used / (1024 ** 3)
        free_ram = ram_info.free / (1024 ** 3)
        ram_info = f"The amount of RAM in a computer determines how much information it can process at once. \n\n" \
                   f"🧠 System RAM: 🧠\n\nTotal: {total_ram:.2f} GB\nUsed: {used_ram:.2f} GB\nFree: {free_ram:.2f} GB\n"
        return ram_info
    except Exception as e:
        return f"An error occurred: {e}"


def get_cpu_info():
    try:
        cpu_info = f"💿 The CPU is the brain of the computer. It processes instructions and performs calculations. " \
                   f"💿\n\nNumber of cores: {psutil.cpu_count()}\nCPU Frequency: {psutil.cpu_freq().max:.2f} MHz "
        return cpu_info
    except Exception as e:
        return f"An error occurred: {e}"


def get_disk_info():
    try:
        disk_info = f"💾 The disk stores all of the information on the computer." \
                    f" 💾\n\nTotal disk space: {psutil.disk_usage('/').total / (1024 ** 3)} GB\n" \
                    f"Total used space: {psutil.disk_usage('/').used / (1024 ** 3)} GB\n" \
                    f"Free disk space: {psutil.disk_usage('/').free / (1024 ** 3)} GB "\
                    f"\n If jarvis output did the match with total space of system then understand." \
                    f" The value for the space available does not include space that is reserved for the root user or " \
                    f"that is used by system files, such as log files, temporary files, and system libraries. As a " \
                    f"result, the value for the space available may be less than the total size of the filesystem. "
        return disk_info
    except Exception as e:
        return f"An error occurred: {e}"


def get_processes():
    try:
        process_list = "📈 The following processes are currently running on the system: 📈\n\n"
        for proc in psutil.process_iter():
            process_list += f"{proc.name()}\n"
        return process_list
    except Exception as e:
        return f"An error occurred: {e}"


def get_ports():
    port_list = "🌐 The following network ports are in use: 🌐\n\n"
    for conn in psutil.net_connections(kind='inet'):
        port = conn.laddr[1]
        pid = conn.pid
        try:
            proc = psutil.Process(pid)
            proc_name = proc.name()
        except psutil.NoSuchProcess:
            proc_name = "unknown"
        port_list += f"Port: {port} | Process ID: {pid} | Process name: {proc_name}\n"
    return port_list
