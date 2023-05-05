You need two terminal to implement the project
Terminal 1:
```
cd ~/cloudnet
sudo ./mdc --vid
```
Terminal 2:
```
cd ~/cloudnet/minidc/controller
ryu-namager controller.py
```
Then you need go back to terminal1 and press <enter>
If you want to change the routing policy, you can use enter controller.py in ~/cloudnet/minidc/controller, in line 26, set the variable self.curpolicy to "default", "static", "vlanAware", "loadBalanced" respectively.
