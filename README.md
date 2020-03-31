

# Prisma Access

When you receive a notification, you must follow a two-step process. First, you must manually or programatically retrieve the IP or loopback addresses. Then, you must update the IP addresses in your organization’s appropriate whitelist to ensure that users do not experience any disruption in service.

Prisma Access sends this notification a few seconds before the new IP address becomes active. We recommend that you use automation scripts to both retrieve and whitelist the new IP addresses.

To add an IP notification URL, complete the following task.

Select PanoramaCloud ServicesConfigurationService Setup.

Add an IP Change Event Notification URL where you can be notified of IP address changes in your Prisma Access infrastructure.

You can specify an IP address or an FQDN to an HTTP or HTTPS web service that is listening for change notifications. Prisma Access sends these notifications from the internet using a public IP address.

You do not need to commit your changes for the notification URL to take effect.


# Prisma Access JSON
This is the JSON (below) Prisma Access will send. The Google function in the python code will parse the json and notify slack and update a channel inside slack

Be Notified of Changes to IP Addresses
To be notified of public IP address changes for remote networks and loopback IP address changes for service connections, remote network connections, and mobile users, you can to specify a URL at which you can be alerted of a change. Prisma Access uses an HTTP POST request to send the notification. This POST request includes the following notification data in JSON format:

    {"addrType": "public_ip", "addrChangeType": "add", "utc_timestamp": "2019-01-31 23:08:19.383894", "text": "Address List Change Notification"}

    {"addrType": "public_ip", "addrChangeType": "delete", "utc_timestamp": "2019-01-31 23:13:35.882151", "text": "Address List Change Notification"}

    {"addrType": "loopback_ip", "addrChangeType": "update", "utc_timestamp": "2019-01-31 23:29:27.100329", "text": "2018-05-11 23:29:27.100329"}


# Python Code
Notification Trigger for Palo Alto Networks Prisma Access to update Slack on a change

This is a basic starter script to get nofied from Prisma Access to update a slack channel when a new external IP gets updated.

https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prisma-access-overview/retrieve-ip-addresses-for-prisma-access.html


# Authentication

https://slack.dev/python-slackclient/auth.html
This shows how to setup authentication securely. In this script it is using just the token in the code which is not recommended.


# Setup Slack Bot 
https://api.slack.com/authentication/basics
Use this guide to setup a Slack App that you can call by the code using one of the authentication methods in the guide.


# Test cURL String
curl -H "Content-type: application/json" -X POST https://google-function -d '{"addrType": "1.2.3.4", "addrChangeType": "add", "utc_timestamp": "2019-01-31 23:08:19.383894", "text": "GP"}' -k


# Google Cloud Function
Go to https://console.cloud.google.com/ and setup a cloud function. Install the python code on this and the requirments file. Once this is deployed it will provide a URL you can use for testing. Once confirmed then it can be deployed to Prisma Access.

