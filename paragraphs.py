import os, sys

para1 = "The protagonist of this story is a young shepherd boy living in a village. Every day, the boy would take his flock of sheep to graze on a nearby hill. One day, while the sheep were grazing, the boy felt bored and decided to play a prank on the people of his village. He cried out as loud as he could.Listening to his cries for help, the villagers rushed to help. And, when they came close, he began laughing. When the villagers understood that the boy had fooled them, they were very angry. Warning him not to play the prank again, they returned. However, the boy indulged in the mischief again a few days later. This time too, the villagers warned the boy before returning to the village.A few days later, the villagers heard the boy's cries for help once again. And, this time, it was for real. However, the villagers were tired of being laughed at and didn't think that the boy was really in trouble. So, they ignored his cries for help. And, the wolf killed and ate all his sheep."

para2 = "There was once a king named Midas who loved gold. One day, God appeared before him and asked him to wish for anything. Being greedy about gold, Midas said, Everything I touch should turn to gold.God granted his wish and told him that, from the next day, everything he touched would turn to gold.Midas was very happy. He woke up early the next morning and went around touching everything and turning them to gold.After a while, Midas felt hungry. He picked up a piece of bread to eat, but it turned to gold. When he picked up a glass of water to quench his thirst, it turned to gold as well. As Midas was thinking about what to do, his daughter rushed to him. And, when Midas touched her, she turned into a golden statue.Miserable and teary-eyed, Midas no longer wanted the boon. He prayed to God and atoned for his greed. Pleased by Midas' prayer, God asked him to wash his hands in the nearby river to get rid of the golden touch.Midas returned after washing his hands and found that everything he had changed to gold had turned back to normal."

para3 = "This is an extremely popular story about a hare and a tortoise.The hare is an animal that is known to move quickly, while a tortoise is one to move slowly.One day, the hare challenged the tortoise to a race simply to prove that he was the best. The tortoise agreed.Once the race began the hare was easily able to get a head start. Upon realizing that the tortoise is far behind. The overconfident hare decided to take a nap.Meanwhile the tortoise, who was extremely determined and dedicated to the race was slowly nearing the finish line. The tortoise won the race while the hare napped. Most importantly he did it with humility and without arrogance."

para4 = "One day, a baby camel was chatting with her mother. She asked, Mother, why do we have humps, round feet, and long eyelashes? Drawing a deep breath, the mother explained, Our humps store water. This helps us survive long journeys in a desert where water is scarce. Our round feet allow us to walk comfortably on sand. And, our long eyelashes protect our eyes from dust and sand, especially during sandstorms. The baby camel remained silent for some time and then asked, 'Mother, why do we stay in a zoo even when we are blessed with so many qualities?'."

para5 = "There was once a lonely elephant. One day, he set out to find friends for himself in the jungle. He found a monkey and asked him if he would be a friend. The monkey refused saying, You can't swing from trees like me. The elephant next met a rabbit and asked him to be his friend. The rabbit refused as well saying, You are too big to enter my burrow. The elephant then met a frog, who also refused, saying, You can't leap like me. The elephant ventured deeper into the jungle where he met a fox. The fox also refused the elephant's friendship saying, You are too big. Disheartened, the elephant returned. However, the next day he decided to go to the jungle again. As he entered the jungle, the elephant found all the animals running to save their lives. He stopped the bear to enquire what had happened.The bear said, The tiger wants to eat us and so we are all running to save ourselves. As the elephant was thinking about what he could do to help the animals, the tiger walked up to him. Mr Tiger, please spare these animals. Do not kill and eat them, the elephant implored. Run or I'll kill and eat you as well, growled the tiger.This angered the elephant and he kicked the tiger. The frightened tiger ran away.All the animals now wanted to be friends with the elephant."

para6 = "Once, a mouse accidentally wakes up a lion. This angers the lion and the mouse begs for his life and promises to pay him back in kind. The lion laughs at this but lets the mouse go. A few days later, the mouse finds the lion trapped in a net and sets the lion free by gnawing on the ropes."

para7 = "This Chinese folklore is about an emperor trying to find a successor. So, he holds a contest in which whoever produces the most beautiful flower from the provided seeds wins. A young gardener is among the contestants, and though he tries his best, he can't get the seed to grow. In the end, he takes his empty pot and displays it among other beautiful flowers. It turns out that the seeds had been cooked so that they would not sprout. He is chosen to be the successor, as he is the only honest contestant."

para8 = "A boy wets his pants in a classroom and is terrified at the prospect of others finding out and ridiculing him. At the same time, a girl and a teacher are walking toward him with a bowl of water. The girl trips and pours the water on his lap. He pretends to be angry with her and the teacher helps them clean the mess. Later the boy asks the girl if she did that on purpose and she replies that she's wet her pants too."

para9 = "Sir Tristram, violer d'amores, fr'over the short sea, had passencore rearrived from North Armorica on this side the scraggy isthmus of Europe Minor to wielderfight his penisolate war: nor had topsawyer's rocks by the stream Oconee exaggerated themselse to Laurens County's gorgios while they went doublin their mumper all the time: nor avoice from afire bellowsed mishe mishe to tauftauf thuartpeatrick: not yet, though venissoon after, had a kidscad buttended a bland old isaac: not yet, though all's fair in vanessy, were sosie sesthers wroth with twone nathandjoe."

para10 = "Computer science is a field of study that involves the design, development, and analysis of computer systems and software. It is a broad and rapidly evolving field that encompasses a wide range of topics, including programming languages, algorithms, data structures, artificial intelligence, databases, networks, securitymore."


def which_para(para_selection):
    if para_selection == "para1":
        return para1
    elif para_selection == "para2":
        return para2
    elif para_selection == "para3":
        return para3
    elif para_selection == "para4":
        return para4
    elif para_selection == "para5":
        return para5
    elif para_selection == "para6":
        return para6
    elif para_selection == "para7":
        return para7
    elif para_selection == "para8":
        return para8
    elif para_selection == "para9":
        return para9
    elif para_selection == "para10":
        return para10
    else:
        return 0

def check_directory(directory_name, req_filename):
    directory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), directory_name))
    if os.path.exists(directory_path):
        image_path = os.path.join(directory_path, req_filename)
        return image_path
    else:
        os.mkdir(directory_path)
        image_path = os.path.join (directory_path, req_filename)
        return image_path


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)