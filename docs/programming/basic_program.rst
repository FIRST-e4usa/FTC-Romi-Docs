Basic Program
=============
This guide will step through creating a basic Blocks program to test that our Romi works.

Programming the Romi works the same way as programming a full-sized FTC robot.
Thus, the following steps also apply to real FTC programming.

Robot Controller Console
------------------------

To access the Robot Controller Console, go to the **Program & Manage** screen of the FTC Romi app:

.. image:: images/menu.png
   :scale: 25 %
   :alt:

.. image:: images/program_and_manage.png
   :scale: 25 %
   :alt:

.. image:: images/connection.png
   :scale: 25 %
   :alt:

From here, you can start programming directly on your phone.
However, it is highly recommended that you program on a computer by connecting it to the phone.

To connect your computer to your phone, connect to the appropriate WiFi network on your computer.
The WiFi name should match the name displayed on the phone's "Program & Manage" screen.
The password is also displayed on the phone's "Program & Manage" screen

.. image:: images/computer_wifi.png
   :scale: 25 %
   :alt:

Once you connect to the phone's WiFi, open a web browser and navigate to ``http://192.168.49.1:8080``.
This should bring up the Robot Controller Console:

.. image:: images/console.png
   :alt:

From here, click the **Blocks** tab at the top. This will take you to this page:

.. image:: images/opmodes.png
   :alt:

Basic POV Drive Sample
----------------------

This page will contain any **OpModes** – programs that control your robot – that you have written.
Since we have not wrote any, it is currently empty.
There are also some buttons on the top. Let’s click on the "Create a New Op Mode" option to create a new program.
This will pop up:

.. image:: images/new_opmode.png
   :alt:

This menu allows you to name your new OpMode and select a sample to base it off of.
For this guide, let's name the OpMode **RomiDrive**. For the **Sample**, select **BasicPOVDrive**.
Then click **OK**.

The new OpMode should have code that looks like this:

.. image:: images/basic_pov.png
   :alt:

The sample **BasicPOVDrive** should already contain basic drive code that can control the Romi!

Running the OpMode
------------------
The OpMode should now be available to select on the phone's Driver Station.
Click `here </docs/programming/app.html#the-driver-station>`_ for a refresher on the Driver Station portion of the FTC app.

Ensure that the Romi is connected to the phone.
Click `here </docs/programming/app.html#connection-status>`_ for a refresher on how to do this.

To run the selected OpMode, press the large "INIT" button to initialize the robot and then press it again to start the robot.
You should now able to connect a gamepad to phone and control the Romi with the joysticks.

Final Setup
-----------

As reference, your final setup (excluding your computer) should look something like this:

.. image:: images/final_setup.jpg
   :alt: Phone, gamepad, and Romi




