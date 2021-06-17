from environs import Env

# ������ ���������� ������ ���������� python-dotenv ���������� environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # �������� �������� ���� str
ADMINS = env.list("ADMINS")  # ��� � ��� ����� ������ �� �������
IP = env.str("ip")  # ���� str, �� ��� ���� ������ �����