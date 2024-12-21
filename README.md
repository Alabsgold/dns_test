How DNS-Based Filtering Works
DNS Resolution: When you type a website URL (e.g., example.com) into your browser, your computer queries a Domain Name System (DNS) server to translate the human-readable domain name into an IP address (e.g., 192.168.1.1), which your browser uses to connect to the site.

Content Filtering: Some DNS services include filtering mechanisms. If the DNS server detects that the domain you're trying to access is flagged as explicit, malicious, or restricted, it will block the request and return a "blocked" page instead of the actual IP address.

Immediate Block: Since the browser never gets the IP address for the site, it can't load the website, and you see the "blocked" message right away.

Who Controls This?
DNS Providers: Certain DNS providers, such as OpenDNS, Cloudflare Family, or Google SafeSearch DNS, offer filtering features. For example:

OpenDNS Family Shield automatically blocks adult content.
Cloudflare Family (1.1.1.3) does the same but can be customized.
Network Administrators: On school, office, or home networks, administrators may configure DNS filtering to block specific types of websites.

Parental Controls: Routers or ISPs may have built-in parental controls that use DNS filtering to block certain categories of sites.

How to Check and Modify This?
Check Your DNS Settings:

On Windows, macOS, or your router settings, see what DNS server is being used. Common ones for filtering are:
208.67.222.123 (OpenDNS Family Shield)
1.1.1.3 (Cloudflare Family)
You can switch to an unfiltered DNS (like 1.1.1.1 from Cloudflare or 8.8.8.8 from Google) if you want unrestricted access.
Use a VPN:

VPNs often bypass DNS filtering by routing traffic through their own private DNS servers.






What the Code Does
Purpose:
The code implements a basic DNS filtering system with an admin panel. It allows users to block explicit websites by their domain name. It works like parental control software to help families prevent access to certain types of content.

Features:

DNS Filtering: Blocks specific domains based on a blocklist.
Admin Panel: A web-based interface for managing the blocklist (adding or removing domains).
Logging: Tracks and logs queries to domains, showing blocked and allowed access attempts.
How It’s Deployed:
The app is built using Flask, a lightweight Python web framework, and it is deployed on a hosting platform like Render. This lets the admin panel run online, accessible via a browser.

How It Works
1. DNS Filtering Functionality
The app acts as an intermediary in the DNS query process:

When a user tries to access a website, the DNS filter checks the domain name against the blocklist.
If the domain is on the blocklist:
The DNS filter blocks access to the website and returns a "blocked" response.
If the domain is not on the blocklist:
The DNS filter allows the query to proceed as usual.
2. Admin Panel
The admin panel provides a simple interface for managing the blocklist:

View the Blocklist: Displays all the currently blocked domains.
Add Domains: Admins can input domain names to add them to the blocklist.
Remove Domains: Admins can remove domain names from the blocklist.
3. Flask Application
The Flask app powers the admin panel and DNS filtering logic:

Routes:

/: Displays the home page of the admin panel.
/add: Allows admins to add domains to the blocklist.
/remove: Lets admins remove domains from the blocklist.
/blocked: Displays all blocked domains for review.
Dynamic Port Binding:

The app dynamically binds to a port specified by the hosting platform using os.environ.get("PORT").
Code Structure
Here’s a simplified breakdown of the app:

Imports:

Standard Python libraries (os for environment variables).
Flask framework (Flask, request, render_template).
Flask Setup:

Initializes the Flask app.
Sets up a secret key for session management (optional).
Routes:

Home Page: Displays a dashboard with the blocklist and controls.
Add Domains: Processes form submissions to add domains to the blocklist.
Remove Domains: Processes form submissions to remove domains from the blocklist.
Blocked Domains: Displays the list of all blocked domains.
Port and Hosting:

Listens on a specific port (provided by the hosting platform).
How Users Interact with It
Admin Logs In:

Visits the web interface hosted on a service like Render.
Manages the Blocklist:

Enters domains to block or unblock them using the admin panel.
DNS Queries Processed:

The DNS filtering system checks each query against the blocklist, blocking or allowing access as needed.
Deployment Details
The app is deployed to a hosting platform like Render, which provides the following:
A public URL for the admin panel.
Automated environment setup, including setting the PORT variable.
Flask runs the app and serves the admin panel at the configured URL.

Ask for Access (if applicable):

If it's a network-controlled filter (like at school or work), you'll need permission from the network admin to access the site.
DNS Logging for Safety:

Some DNS filters log blocked attempts for monitoring purposes, like keeping track of which websites users attempt to access.
