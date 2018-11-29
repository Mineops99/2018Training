import settings
import si_game

#if you can see this, Hi from DrKittyKat!
#create our settings. Incase we need to load diffrent values
settings = settings.Settings()

#create the game instance
game = si_game.Si_Game(settings)


#run the game. Does not return until exit.
game.run_game()