# Generated by Django 2.2 on 2020-11-06 08:26

from django.db import migrations
from webapp.models.episode import Episode

def insert_episodes(apps, schema_editor):
    Episode.objects.create(episode_number=4,title='Cancelled',screenshot_url='https://static.wikia.nocookie.net/southpark/images/e/e6/Cancelled15.jpg/revision/latest?cb=20150515223918', season=7, synopsis='The boys learn that Earth is a reality show for aliens and must save it from cancellation.', rating=7)
    Episode.objects.create(episode_number=2,title='Krazy Kripples',screenshot_url='https://static.wikia.nocookie.net/southpark/images/8/8a/702_image_17.jpg/revision/latest?cb=20061016225724', season=7, synopsis='Timmy and Jimmy start a club for cripples. Christopher Reeve comes to town to promote stem cell research.', rating=7)
    Episode.objects.create(episode_number=3,title='Toilet Paper',screenshot_url='https://static.wikia.nocookie.net/southpark/images/6/61/Toilet_Paiper_HD.png/revision/latest?cb=20120630131429', season=7, synopsis='Kyle feels guilty after he and the boys TP their art teacher\'s house.', rating=7)
    Episode.objects.create(episode_number=1,title='I\'m a Little Bit Country',screenshot_url='https://static.wikia.nocookie.net/southpark/images/f/fd/ImaLittleBitCountry13.jpg/revision/latest?cb=20100421005631', season=7, synopsis='The boys enter an anti-war demonstration; Cartman travels back in time to the American Revolutionary War era.', rating=7)
    Episode.objects.create(episode_number=5,title='Fat Butt and Pancake Head',screenshot_url='https://static.wikia.nocookie.net/southpark/images/a/a8/FatButtandPancakeHead06.jpg/revision/latest?cb=20100418055907', season=7, synopsis='Cartman\'s hand puppet Jennifer Lopez gets major publicity, which angers the real Jennifer Lopez.', rating=7)
    Episode.objects.create(episode_number=6,title='Lil\' Crime Stoppers',screenshot_url='https://static.wikia.nocookie.net/southpark/images/2/23/LilCrimeStoppers08.jpg/revision/latest?cb=20100310164623', season=7, synopsis='The boys pretend to be police detectives.', rating=7)
    Episode.objects.create(episode_number=7,title='Red Man\'s Greed',screenshot_url='https://static.wikia.nocookie.net/southpark/images/5/5c/ManMansGreed07.jpg/revision/latest?cb=20100303185620', season=7, synopsis='The town is taken over by Native Americans who want to create a highway.', rating=7)
    Episode.objects.create(episode_number=8,title='South Park is Gay!',screenshot_url='https://static.wikia.nocookie.net/southpark/images/5/53/SouthParkisGay03.jpg/revision/latest?cb=20100315061138', season=7, synopsis='The men and boys of town become metrosexual.', rating=7)
    Episode.objects.create(episode_number=9,title='Christian Rock Hard',screenshot_url='https://static.wikia.nocookie.net/southpark/images/1/16/ChristianRockHard10.jpg/revision/latest?cb=20100407054638', season=7, synopsis='Cartman, Token, and Butters form a Christian music band. Stan, Kyle, and Kenny learn about downloading free music off the Internet.', rating=7)
    Episode.objects.create(episode_number=10,title='Grey Dawn',screenshot_url='https://static.wikia.nocookie.net/southpark/images/c/c5/GreyDawn01.jpg/revision/latest?cb=20100506004235', season=7, synopsis='The elderly have their driver\'s licenses taken away, against which the AARP retaliates.', rating=7)
    Episode.objects.create(episode_number=11,title='Casa Bonita',screenshot_url='https://static.wikia.nocookie.net/southpark/images/8/8f/CasaBonita02.jpg/revision/latest?cb=20100503001904', season=7, synopsis='Cartman tries to get himself invited to Kyle\'s birthday party at Casa Bonita, a Disneyland-like Mexican restaurant.', rating=7)
    Episode.objects.create(episode_number=12,title='All About Mormons',screenshot_url='https://static.wikia.nocookie.net/southpark/images/7/7d/AllAboutMormons04.jpg/revision/latest?cb=20100420235307', season=7, synopsis='Stan befriends a boy and his family, who are all Mormons.', rating=7)
    Episode.objects.create(episode_number=13,title='Butt Out',screenshot_url='https://static.wikia.nocookie.net/southpark/images/d/de/ButtOut02.jpg/revision/latest?cb=20100401001206', season=7, synopsis='The town calls in Rob Reiner to combat the spread of smoking among children after the boys are caught doing so.', rating=7)
    Episode.objects.create(episode_number=14,title='Raisins',screenshot_url='https://static.wikia.nocookie.net/southpark/images/f/f6/Raisins04.jpg/revision/latest?cb=20100412020415', season=7, synopsis='The boys take Stan to Raisins, a Hooters-like restaurant after Wendy breaks up with him. Butters meets a girl who seems interested in him.', rating=7)
    Episode.objects.create(episode_number=15,title='It\'s Christmas in Canada',screenshot_url='https://static.wikia.nocookie.net/southpark/images/4/48/ChristmasinCanada18.jpg/revision/latest?cb=20100420234139', season=7, synopsis='Kyle and the boys fly to Canada during Christmastime to see the Canadian Prime Minister after Ike\'s biological parents take him back to Canada.', rating=7)


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_season_3_to_7'),
    ]

    operations = [
        migrations.RunPython(insert_episodes)
    ]
