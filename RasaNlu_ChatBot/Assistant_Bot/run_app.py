from rasa_core.channels.rest import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/assistantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)
input_channel = SlackInput('xoxp-577750409252-577782185266-623450917824-9f928829e771f94acc084958e634f15a',
                            'xoxb-577750409252-611978780099-2gV3498zVOYKckxFbbxtuTKP',
                            'n98DSijgCdAVc4DJ2oL9VPtt',
                             True)
agent.handle_channel(HttpInputChannel(5004,'/',input_channel))


