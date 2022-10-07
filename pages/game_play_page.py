from pages.base_page import BasePage
from altunityrunner import By 

class GamePlayPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    @property
    def pause_button(self):
        return self.altdriver.wait_for_object(By.NAME,'Game/WholeUI/pauseButton', timeout=2)
    
    @property
    def character(self):
        return self.altdriver.wait_for_object(By.NAME,'PlayerPivot', timeout=2)

    def is_displayed(self):
        if self.pause_button and self.character:
            return True

    def press_pause(self):
        self.pause_button.tap()

    def get_current_life(self):
        return int(self.character.call_component_method("CharacterInputController", "get_currentLife", parameters=[]))

    def avoid_obstacles(self, number_of_obstacles=10):
        character = self.altdriver.find_object(By.NAME,"PlayerPivot")
        #set character to be invincible for this method
        # character.call_component_method("CharacterInputController", "CheatInvincible", "true")
        moved_left = False
        moved_right = False

        for i in range(0, number_of_obstacles):
            all_obstacles_unsorted = self.altdriver.find_objects_which_contain(By.NAME,"Obstacle")
            all_obstacles = sorted(all_obstacles_unsorted, key=lambda k: float(k.worldZ))
            obstacles = []
            for o in all_obstacles:
                if (float(character.worldZ) < float(o.worldZ)):
                    obstacles.append(o)
            obstacle = obstacles[0]
           
            while(float(obstacle.worldZ) - float(character.worldZ) > 5):
                obstacle = self.altdriver.find_object(By.ID,obstacle.id)
                character = self.altdriver.find_object(By.NAME,"PlayerPivot")
        
            if "Barrier" in obstacle.name or "Rat" in obstacle.name:
                character.call_component_method("CharacterInputController", "Jump", parameters=[])
            else:
                if float(obstacle.worldZ) == float(obstacles[1].worldZ):
                    if float(obstacle.worldX) == float(character.worldX):
                        if float(obstacles[1].worldX) == -1.5:
                            character.call_component_method("CharacterInputController", "ChangeLane", parameters=["1"])
                            moved_right = True
                        else:
                            character.call_component_method("CharacterInputController", "ChangeLane", parameters=["-1"])
                            moved_left = True
                    elif float(obstacles[1].worldX) == float(character.worldX):
                        if float(obstacle.worldX) == -1.5:
                            character.call_component_method("CharacterInputController", "ChangeLane", parameters=["1"])
                            moved_right = True
                        else:
                            character.call_component_method("CharacterInputController", "ChangeLane", parameters=["-1"])
                            moved_left = True
                elif float(obstacle.worldX) == float(character.worldX):
                    character.call_component_method("CharacterInputController", "ChangeLane", parameters=["1"])
                    moved_right = True
            while (float(character.worldZ) < float(obstacle.worldZ) and float(character.worldX) < 99):
                obstacle = self.altdriver.find_object(By.ID,obstacle.id)
                character = self.altdriver.find_object(By.NAME,"PlayerPivot")
            if moved_left:
                character.call_component_method("CharacterInputController", "ChangeLane", parameters=["1"])
                moved_left = False
            if moved_right:
                character.call_component_method("CharacterInputController", "ChangeLane", parameters=["-1"])
                moved_right = False
