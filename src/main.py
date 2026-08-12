from src.client import CommunicationManager

if __name__ == '__main__':
    cM = CommunicationManager()
    print(cM.get_version())
