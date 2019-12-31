# Conway's Game of Life
[the famous Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using tkinter and numpy<br/>

The Glider shape
 
![](Animated GIF-source.gif)

# Description
Project consists of two modules lis and Gui<br> 
* lis contain Mop class for mathematical operation on lists
* Gui contain Vis class for handling the Gui

## Usage

```python
ly.init_pos(row,column) # intialize the live cells
m.colorize(ly.l) # color the living cells with red given the list
ly.next_it() # calculate the next shape 
m.top.after(1000,again) # delay between every object in milliseconds
```