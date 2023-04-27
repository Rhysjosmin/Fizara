from bs4 import BeautifulSoup
html_List = [
  '''


  <section id="Yogasanas">
    <div class="Yoga" data-aos="fade-right">
      <img
        src="../../../media/images/Yoga/StandingSideStretch.png"
        alt=""
      />
      <div>
        <h1>Standing Side Stretch</h1>
        <p>
          Target areas: Shoulders and upper back. Benefits: Reduces back
          pain, improves upper body flexibility and reduces shoulder
          stiffness (especially if you work in an office for most of the
          day). How to do it: Stand in the classic mountain pose (Tadasana)
          with your arms at your sides, your big toes touching each other
          and your heels slightly spread apart. Raise your arms and
          interlace your fingers over your head with your index fingers
          pointing upwards. Draw an invisible arch with your arms, extending
          them to your side as far as you can while pushing your hip in the
          opposite direction. Make sure you keep your arms straight. Move
          your arms back to center and stretch to the other direction,
          holding the pose at maximum range for 30-60 seconds at a time. You
          can also try doing this pose while seated (the sitting side
          stretch).
        </p>
      </div>
    </div>
    <div class="Yoga" data-aos="fade-right">
      <img
        src="../../../media/images/Yoga/Bound Angle Pose.png"
        alt=""
      />
      <div>
        <h1>Bound Angle Pose</h1>
        <p>
          Target areas: hips, thighs and knees.
          Benefits: Opens hips and thighs wider for easier childbirth, eases knee pain, helps with sore or swollen feet and reduces overall body fatigue.
          How to do it: Sit on the floor with your legs stretched straight in front of you. Bend your knees and pull your heels closer to your pelvis. Drop your knees sideways as far as they can get. Don’t force them all the way down if your hips are tight. Just try to relax your thighs and hips as much as you can.
          With your thighs to the sides and the soles of your feet pressing against each other, try to pull in your heels as much as you can. Then grasp the big toe or ankle of each foot with your hands.
          Hold this pose for 1-5 minutes. Repeat it regularly if your hips and groin feel tight. It will improve flexibility and open up your hips.
          
        </p>
      </div>
    </div>
    <div class="Yoga" data-aos="fade-right">
      <img
        src="../../../media/images/Yoga/Yoga Squat.png"
        alt=""
      />
      <div>
        <h1>Yoga Squat</h1>
        <p>
          Target areas: belly, hips and pelvis.
          Benefits: This is one of the best poses if your hips are feeling too tight. It also helps to widen the pelvis which makes childbirth easier.
          How to do it: Sit on the floor with your legs spread out in front of you. Bend your knees upwards one at a time, bringing your foot as close to your butt as possible. The knees should be slightly wider than your shoulder width.
          Slowly lift off your butt, putting weight onto your feet and hold that lifted pose for several seconds.
          If this feels too strenuous you can also try a supported yoga squat where you sit on a low stool or block.
        </p>
      </div>
    </div>
    <div class="Yoga" data-aos="fade-right">
      <img
        src="../../../media/images/Yoga/Easy Pose.png"
        alt=""
      />
      <div>
        <h1>Easy Pose (Sukhasana)</h1>
        <p>
          Target areas: back and hips.
          Benefits: This is more of a meditation pose. It calms the mind and helps fight stress and anxiety. It’s also great for opening up the hips and reducing lower back pain.
          How to do it: Sit on a yoga mat and cross your shins. The soles of your feet should be facing outwards under the opposite leg. Your legs should form a triangle with your crossed shins forming a sort of a straight line.
          You can lay your hands on your knees with the palms facing up or down. If you feel uncomfortable, fold a blanket and sit on it.
          Hold this pose for as long as you feel comfortable then cross your shins the other way and hold again.
          Feel free to try some relaxing meditation.              
        </p>
      </div>
    </div>
    <div class="Yoga" data-aos="fade-right">
      <img
        src="../../../media/images/Yoga/Important Breathing Tips.png"
        alt=""
      />
      <div>
        <h1>Important Breathing Tips</h1>
        <p>
          The most important element in postpartum yoga is your breathing. Something that separates yoga from other kinds of exercise is the fact that each posture is linked to inhale and exhale. Why so much heavy breathing?
          Breathing and moving together sets the pace of your practice. It also helps you move more deeply into postures, says Larson. Deep breathing—long, full inhales and exhales—also brings oxygen to the entire body, which energizes your system. Here are the basics of yoga breathing:
          Inhale through your nose; fill your belly, ribs, and upper chest with air so that they puff out in front of you.
          Exhale through your nose and tuck in your belly button as the air is being released.
        </p>
      </div>
    </div>

  </section>
  ''',
  '''

  <section id="Yogasanas">
  
    <div class="Yoga" data-aos="fade-right">
      <img src="../../../media/images/Yoga/Plank Vinyasa.png" alt="" />
      <div>
        <h1>Plank Vinyasa</h1>
        <p>
          Get down on all fours with your wrists under your shoulders. Place
          a folded blanket under your wrists if you need support, or lower
          onto your forearms. To get into Plank position, straighten one leg
          at a time behind you, balancing on the balls of your feet, abs
          pulled up and in, and head in line with your spine (i.e., neither
          straining up nor hanging down). Elongate your spine and press into
          the balls of your feet. Inhale, then exhale as you draw your right
          knee in toward your chest, contracting the muscles in your lower
          belly (shown). Return to Plank position, then switch legs.
          Alternate knee tucks for 8 to 20 reps. Benefits: Increases stamina
          and strength, especially in your deep abdominal and back muscles.
        </p>
      </div>
    </div>
    <div class="Yoga" data-aos="fade-right">
      <img src="../../../media/images/Yoga/Loctus Pose.png" alt="" />
      <div>
        <h1>Loctus Pose</h1>
        <p>
          Lie flat on your belly with your legs hipwidth apart on the floor.
          Rest your head on your hands (A). Clasp your hands behind your
          lower back to open through your chest and shoulders. Keep your
          spine long and squeeze your buttocks, pressing your hips into the
          floor as you lift your head, shoulders and legs off the mat,
          keeping your neck in line with your spine. As you lift your legs
          up and out, tuck your tailbone under and keep your belly
          contracted and pulled away from the floor (B). Hold for 3 to 5
          breaths, then lower to starting position. Repeat for 2 to 3 reps.
          Benefits: Strengthens the deep back muscles of the core and opens
          your chest and shoulders, improving posture and relieving
          lower-back and upper-body strain.
        </p>
      </div>
    </div>
    <div class="Yoga" data-aos="fade-right">
      <img src="../../../media/images/Yoga/Pelvic Tilts.png" alt="" />
      <div>
        <h1>Pelvic Tilts</h1>
        <p>
          For this gentle postpartum yoga position, lie on your back with
          feet hip-width apart, your arms straight at your sides and palms
          down. Curl your tailbone under slightly, feeling your spine settle
          into the floor, which relieves pressure in the low back. Inhale,
          then exhale as you lift your hips up slowly, tilting your pelvis
          as you tuck your tailbone under and scoop your lower belly in
          (shown). Hold for 1 to 2 breaths, then lower to starting position.
          Repeat for 5 to 10 reps. Benefits: Strengthens the upper and lower
          back, hips and legs. Brings awareness and strength to the pelvic
          floor and lower belly.
        </p>
      </div>
    </div>
    <div class="Yoga" data-aos="fade-right">
      <img src="../../../media/images/Yoga/Legs Wide Pose.png" alt="" />
      <div>
        <h1>Legs Wide Pose</h1>
        <p>
          Lie on your back and lift your legs so your body forms a letter
          "L." Lace your hands behind your head as you squeeze your ab
          muscles. Exhale as you lift your shoulders off the floor. Separate
          your legs a few inches, reaching one arm forward and between your
          legs. Contract your lower belly as you reach (shown). Keep your
          upper body lifted as you bring your legs together and place your
          hands back behind your head. Switch sides and repeat for 8 to 10
          reps. Benefits: Strengthens the deep abdominal muscles and
          stretches the hamstrings.
        </p>
      </div>
    </div>
  </section>
  '''
]

# html=html_List[1]
for i,html in enumerate(html_List):
    soup = BeautifulSoup(html, 'html.parser')

    sections = soup.find_all('section', {'id': 'Yogasanas'})
    res=''
    for section in sections:
        yogas = section.find_all('div', {'class': 'Yoga'})

        for yoga in yogas:
            image = yoga.find('img')['src']
            heading = yoga.find('h1').text.strip()
            paragraphs = []
            try:
                ul = yoga.find('ul')
                for li in ul.find_all('li'):
                    paragraphs.append(f"''{li.text.strip()}''")
            except:
                p = yoga.find('p')
                paragraphs.append(f"''{p.text.strip()}''")
            data = {
                'heading': heading,
                'paragraphs': paragraphs,
                'image': image
            }

            res += str(data) 


    with open(f'./file{i}.json' ,'w') as f:
        f.write(res)
        f.close()
