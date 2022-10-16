import audio_player_file_checker
import logging
from ui.gui import AudioPlayerUi

if __name__ == '__main__':
    if not audio_player_file_checker.check_files():
        logging.critical("Exiting program due to file checking error.")
        exit(1)
    
    player = AudioPlayerUi()
    player.start()
    """try:
        player = AudioPlayerUi()
        player.start()
    except Exception as e:
        logging.critical("Exiting program abnormally.")
        logging.critical(e)
        exit(1)
    logging.info("Exiting program normally.")"""
    