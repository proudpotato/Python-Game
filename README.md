# PYTHON GAMES: my product

1. **參考資料**
    1. Pygame Page: http://pygame.org
    2. documentation: http://pygame.org/docs/ref/
    3. ~~XXX忘記了~~<br><br>
------

**_2. What is Pygame_**:
  * Pygame提供Display, Sound, Music, Image, Text, Event幫助製作遊戲
  * Pygame可以做出2-D小遊戲
  * Pygame偵測使用者使用Keyboard, joystick, mouse控制遊戲
  * Pygame提供許多內建的game objects來製作遊戲<br><br>

**_3. PYGame Basic Codes_**:
| Code | Description |
|:-----:|:----------:|
|_1.py_ | Create my game surfaces, game loop and drawing.|
|_2.py_ | Create text, font, sound and image objects.    |
|_3.py_ | Getting user keyboard and collision dection.   |

**_4. Code snippet_**
```python
#Create game display
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Hungry Whale!")

```
```python
#Blit image object and setting its rec.
player_image = pygame.image.load("whale.png")
player_rect = player_image.get_rect()
player_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT-32)
displayscreen.blit(player_image, player_rect)
```
**_5. Game Assets:_**
    * .[Icon Archive:].(https://iconarchive.com/) 網站提供很多遊戲角色下載
    * .[Leshy SFMaker:].(https://www.leshylabs.com/apps/sfMaker/) 網站可以下載遊戲特效，也可以簡單自己自做音效
