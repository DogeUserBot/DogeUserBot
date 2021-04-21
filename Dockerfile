# Copyright © 2021 Doge UserBot in Telegram App
# All rights reserved.
#
# Licensed under the Doge UserBot Public License;
# you may not use this file except in compliance with the License.
#
# @MUTLCC | @SanalMafya
#
FROM dogeuserbot/dogeuserbot:latest
WORKDIR /root/DOGE/
RUN git clone https://github.com/DogeUserBot/DogeUserBot.git /root/DOGE
RUN pip3 install -r requirements.txt
CMD ["python3", "doge.py"]
