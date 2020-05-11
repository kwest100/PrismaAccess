
import slack

def update_ip(request):
    
    request_json = request.get_json()
    if request_json:
        p_ip  = request_json['addrType']
        c_type = request_json['addrChangeType']
        t_stp  = request_json['utc_timestamp']
   
        #This method is insecure. Be sure to change this to Oauth in Production
        client = slack.WebClient(token="Bot User OAuth Access Token")

        response = client.chat_postMessage(
            channel='#general',
            text="Result : {} {} {}".format(p_ip, c_type, t_stp))
        assert response["ok"]
        assert response["message"]["text"] == "Result : {} {} {}".format(p_ip, c_type, t_stp)

        return ("Result : {} {} {}".format(p_ip, c_type, t_stp))
