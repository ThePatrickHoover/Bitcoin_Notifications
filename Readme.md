# How to Set-Up:

PC:
 ⋅⋅* Download and install [Python](https://www.python.org/downloads/) on your computer.
 ⋅⋅* Download script.
 Mobile Device:
 1. [Create a new applet.](https://ifttt.com/create)
 1. Click "this".
 1. Select "Webhooks".
 1. Set-Up Webhooks and make a Text file called "Key.txt" and put your 21-digit key in that file. Save and close.
 1. Click the box labeled "Receive a web request".
 1. Name your applet **bitcoin_price_update**.
 1. Click "that".
 1. Select "Telegram".
 1. Click the box labeled "Send Message" (*you may have to set up telegram and link IFTTT on your phone*).
 1. Set the Message text to `'Latest Bitcoin price: <br>{{Value1}}'.`
 1. Complete. Run the script with Key.txt in the same folder
