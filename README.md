<h1>Lepy - Learn Python (Antivirus)<br>School Project</h1>
<p>This project contains my source code for an USB scanner using ClamAV (Open source virus scanner) and a Raspberry PI 4<p>
<h2>Requirements</h2>
<ul>
  <li>Raspberry Pi 4</li>
  <li>Python installed</li>
  <li>fstab installed</li>
  <li>ClamAv package installed</li>
 </ul>
 <h2>
 About this project:
 </h2>
 <p>
 
The idea of creating a device to scan USB sticks for malicious content is an interesting one, and one that can be easily achieved with the right materials and tools. The device should be able to detect malicious data. The Raspberry Pi 4 can provide us with plenty of computing power, and should be more than capable of accomplishing this task.

The first step in creating this device is to identify the parts we will need and the steps we will have to take to get the device up and running. The Raspberry Pi 4 is the most important part of the device. It will be the main computing power and will be responsible for scanning the USB stick and identifying any malicious data. We will also need multiple USB sticks to use as a test devices, to make sure the device is working correctly. We will then need a monitor / computer that has the possibility to connect to the Raspberry Pi using a Browser.
Once we have all the parts together, the next step is to set up the Raspberry Pi and install the necessary software. The Raspberry Pi should run a Linux operating  in my case Raspberry PI OS without a UI system and should have the necessary packages installed to allow it to connect to the USB stick for example fstab is needed. We will also need to install a malware scanner that can be used to scan the USB stick. I used ClamAV because it is a trusted Open Source virus scanner. Once the device is set up, we can begin to develop the code that will allow us to detect malicious data and display it to the end user.

Once the code is written and tested, the device should be ready to use. The user should be able to plug in a USB stick and the device will scan it automatically without the user doing anything then plug in the USB stick in one of the 4 available slots. And later on he should see the result in his browser.
The device should be a useful tool for anyone who needs to ensure that their USB sticks are free from malicious data. It should also be a useful tool for anyone who needs to check USB sticks from untrusted sources, as it will allow them to quickly scan the USB stick. And be aware if there is any malicious content on the USB stick. With a bit of time and effort, creating a device to scan USB sticks for malicious data should be a relatively straightforward task.
By creating a device like this, we can help to ensure that our data is safe and secure, and that we can trust any USB sticks we receive from untrusted sources.
Additional Information: The project uses some shell script for plug in the USB stick automatically, and there is a mix between multiple programming languages, the whole “backend” is coded using python to manage the queues, and for visual representation in the browser javascript & css is used.
</p>

<h2>Additional Info</h2>
The webserver.py needs to be located next to the other files to work properly


<h2> Currently Working on redesigning display code</h2>
