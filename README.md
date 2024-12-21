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
Ask for Access (if applicable):

If it's a network-controlled filter (like at school or work), you'll need permission from the network admin to access the site.
DNS Logging for Safety:

Some DNS filters log blocked attempts for monitoring purposes, like keeping track of which websites users attempt to access.
