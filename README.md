# Groups Plugin for CraftBeerPi 3.0
With this plugin you can create both Actor Groups and Sensor Groups.  When you group actors together, a single group will turn on, turn off, or set power on all actors at the same time.  When you group sensors together, a single group will show the average of the sensors within that group.  You can even create groups where the members of that group are *other* groups.

:warning:***IMPORTANT:*** Please make sure you update CraftBeerPi 3.0 to the latest version available before installing this plugin. It requires a feature that was introduced on July 8, 2017.

## Video
![groups_actordemo](https://user-images.githubusercontent.com/29404417/28087816-cbbab528-6651-11e7-9153-768c13ab438c.gif)

## Creating an Actor Group
1.  Navigate to the **System** menu and select **Hardware Settings**.
2.  Under Actors, click **Add** and fill out the following properties:
    1.  **Name**: Give this group a name, typically one that is descriptive of its purpose is best. *example: All Pumps, Mash Recirculation, Chill Wort*
    2.  **Type**: Select ActorGroup
    3.  **Actor 1-8**: Select which actors should be a part of this group.
    4.  Click **Add** when done

You will now see the ActorGroup on the dashboard.  You can turn it on, off, or set power to it as if it were any ordinary actor, except it will perform the same operation on all of the actors within the group.  Add the group to any brew step or kettle/fermentator that lets you select actors, except make sure all of the actors within that group will handle the type of logic that is being used by that device.  For example, don't put a pump in a group that is assigned to a heating element that uses PID logic to be controlled, because pumps don't like being turned on and off rapidly.

## Creating a Sensor Group
1.  Navigate to the **System** menu and select **Hardware Settings**.
2.  Under Sensors, click **Add** and fill out the following properties:
    1.  **Name**: Give this group a name, typically one that is descriptive of its purpose is best. *example: Fermentation Chamber Sensors, Boil Kettle Sensors*
    2.  **Type**: Select SensorGroup
    3.  **Sensor 1-8**: Select which sensors should be a part of this group. If you are choosing sensors that have different units, the group will register its unit as the same unit that Sensor 1 is using.
    4.  Click **Add** when done
    
You will see your SensorGroup on the dashboard with your other sensors readings.  You can assign a sensor group to any device that allows you to select a sensor, so you could use it to get a good overall reading of a large fermentation chamber using multiple sensors spread throughout it, or if you have a large mash tun you could have one sensor near the top, one near the bottom, and then average their readings.
