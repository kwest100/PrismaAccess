
import slack

def update_ip(request):
    
    request_json = request.get_json()
    if request_json:
        p_ip  = request_json['addrType']
        c_type = request_json['addrChangeType']
        t_stp  = request_json['utc_timestamp']
   

        client = slack.WebClient(token="xoxb-484624014260-500455962290-dsj7B4GMgtPAlraFB6VNdYI0")

        response = client.chat_postMessage(
            channel='#general',
            text="Result : {} {} {}".format(p_ip, c_type, t_stp))
        assert response["ok"]
        assert response["message"]["text"] == "Result : {} {} {}".format(p_ip, c_type, t_stp)

        return ("Result : {} {} {}".format(p_ip, c_type, t_stp))
