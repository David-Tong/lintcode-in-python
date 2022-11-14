class Solution:
    """
    @param stations: an integer array
    @param k: an integer
    @return: the smallest possible value of D
    """
    def minmax_gas_dist(self, stations, k):
        # Write your code here
        L = len(stations)
        MAX_DIST = 0
        for x in range(1, L):
            MAX_DIST = max(MAX_DIST, stations[x] - stations[x - 1])

        def is_possible(stations, k, dist):
            total = 0
            for x in range(1, L):
                total += int((stations[x] - stations[x - 1]) / dist)

            if total > k:
                return False
            else:
                return True

        SCALE = 1e-6
        left = 0
        right = MAX_DIST
        while left + SCALE < right:
            middle = (left + right) / 2.0
            if is_possible(stations, k, middle):
                right = middle
            else:
                left = middle + SCALE

        if is_possible(stations, k, left):
            return left
        else:
            return right


stations = [1,2,3,4,5,6,7,8,9,10]
k = 9

stations = [3,6,12,19,33,44,67,72,89,95]
k = 2

stations = [0,5,8,16,33,61,62,74,83,93]
k = 10

stations = [5143,57422,83829,128398,132775,135996,229623,283808,431763,455707,490810,530642,564121,596433,721125,766325,836536,843525,866065,879660,886086,951321,957889,996721,1053484,1080327,1166840,1222536,1227967,1331365,1364179,1370670,1423817,1427717,1483250,1496819,1515829,1595123,1672943,1695727,1722404,1760428,1778317,1810996,1863335,1902979,1914122,1975304,2018748,2130266,2160787,2251044,2328583,2466523,2501013,2537035,2577017,2747248,2807716,2822036,2970097,3089237,3090530,3117374,3258095,3287516,3307771,3350806,3432495,3464487,3468938,3477610,3491645,3495198,3574704,3603258,3608250,3621863,3638290,3646971,3738299,3886375,3907886,3908667,3911927,3977950,4080271,4084692,4242458,4242858,4280191,4286680,4352301,4375727,4385956,4406879,4412879,4434642,4511011,4579939,4805850,4823010,4936284,5031577,5195258,5208142,5249858,5261218,5321603,5348863,5363489,5368883,5488110,5649017,5660421,5840620,5885998,5948721,5983079,6034006,6172280,6179107,6255172,6358292,6461776,6464334,6464404,6493106,6542440,6579331,6636280,6728229,6768243,6768258,6787381,6844401,6927540,7040280,7062511,7315743,7328067,7328813,7334028,7346108,7377439,7459566,7581200,7625331,7644954,7672692,7705707,7793710,7849161,7849907,7900190,7969930,8015765,8037944,8078320,8095495,8128982,8232109,8286480,8320912,8321505,8373777,8381941,8530411,8610103,8647022,8675329,8688484,8774301,8891132,8935075,8954718,8970989,8997211,9011166,9066885,9067066,9109872,9127868,9233483,9256574,9261374,9372480,9409697,9410909,9431797,9480142,9574742,9587712,9604431,9605898,9709683,9744846,9747303,9776453,9922086,9976559,10104591,10167707,10208158,10252282,10256359,10366787,10413917,10414679,10426854,10482827,10546328,10579923,10751780,10763795,10785550,10824331,10847287,10871986,10993032,10996126,11091805,11092866,11118555,11204407,11264242,11264549,11272686,11388350,11414211,11417377,11461703,11515136,11580144,11659379,11762939,11774084,11836548,11856782,11867671,12014469,12020445,12032487,12037471,12073074,12102386,12173196,12194046,12257309,12284162,12292063,12301325,12376674,12389260,12431100,12552945,12575352,12589684,12601504,12681569,12752046,12775449,12815246,12829379,12871649,12917165,12962456,12964883,13169558,13175343,13261973,13406008,13443996,13486533,13511891,13516404,13546002,13551942,13579245,13602952,13705803,13781861,13793776,14036734,14046392,14060762,14068448,14111074,14165671,14370071,14376946,14431087,14538852,14624964,14751381,14814177,14837175,14840169,14957772,15048120,15111449,15220362,15290653,15367663,15412656,15437107,15439723,15613512,15660991,15680360,15708291,15713889,15916674,16076845,16108400,16241954,16295174,16387224,16447020,16450987,16482083,16489166,16507383,16513597,16600210,16614975,16628076,16656427,16721645,16732700,16742772,16753012,16753372,16757939,16758525,16760538,16761459,16846403,16874880,16998192,17024851,17118352,17141917,17182226,17318861,17326689,17330727,17404134,17430493,17442281,17530306,17619082,17622743,17794654,17852010,18091432,18140778,18223904,18288938,18354994,18386470,18444545,18462688,18489875,18557575,18606354,18630726,18673594,18689856,18707509,18762792,18763644,18803573,18851982,18877379,18931001,18956284,19065464,19078895,19390378,19408626,19415654,19448328,19520423,19571370,19640360,19643451,19650052,19716938,19718332,19750181,19783354,19785066,19834267,19874475,19901396,19967531,19971241,19979049,20017180,20030811,20054874,20078391,20187907,20244920,20359982,20361705,20462489,20491065,20689398,20799569,20840739,20880222,20888454,21030824,21105714,21130103,21161504,21163505,21176961,21205458,21364348,21461061,21503581,21627749,21805307,21842729,21945235,22013347,22111565,22134113,22212158,22266715,22275759,22320962,22339579,22436486,22532844,22565332,22589071,22597434,22626420,22649091,22657360,22684933,22727846,22747362,22865432,23018813,23061950,23094286,23130488,23186817,23233575,23298232,23440132,23442563,23443583,23519874,23531944,23571218,23613428,23649801,23683405,23691197,23735632,23806240,23862208,23910275,23912274,24055077,24233575,24271052,24389053,24429379,24504175,24656169,24771475,24940808,24962060,24997450,25002957,25049635,25175509,25240276,25263846,25284896,25290103,25324114,25392408,25424406,25425915,25523785,25782743,25791742,25821679,25840286,25840976,25873820,26038623,26048103,26120555,26182018,26223272,26272669,26298580,26308246,26386530,26408870,26519356,26524955,26550358,26629739,26679826,26743294,26761608,26853831,26862595,26908547,26912968,26974394,26992103,27007156,27053343,27071635,27074929,27287475,27364539,27470123,27592290,27655368,27717571,27771354,27788987,27793343,28014187,28075145,28130087,28153536,28191477,28238874,28270664,28320268,28323021,28370715,28461009,28494876,28510215,28540122,28608276,28757561,28764088,28838663,28861450,28904387,28920316,29158031,29174885,29196462,29218358,29250667,29275539,29332993,29411957,29618965,29659101,29748424,29772474,29774789,29829585,29863365,29873492,29874897,29876378,29888494,29903712,29956059,30007494,30020085,30143503,30204696,30363408,30420811,30435815,30438048,30470211,30485572,30521754,30531560,30570591,30870398,30925120,30928571,30938851,30964568,31018550,31110233,31149325,31623858,31767515,31769787,31869107,31924938,31956785,31971659,31982979,32061767,32137492,32284232,32312819,32315032,32382414,32404695,32461122,32504883,32516344,32523624,32571323,32579283,32607733,32780941,32818832,32853314,32867826,32895267,32947095,32953147,33119087,33130620,33141853,33172182,33214707,33272504,33293013,33382492,33448215,33531694,33605970,33684246,33809923,33848257,33868123,33937503,33960872,34029141,34164658,34195376,34207762,34296391,34336847,34382993,34412255,34434850,34439675,34445907,34480106,34506509,34624121,34714342,34719916,34769932,34821451,34943252,35064562,35118555,35156187,35160155,35179020,35343994,35351582,35360240,35538580,35541355,35562740,35565866,35567706,35632778,35714248,35715224,35792948,35797956,35804519,35885035,35887327,35930792,35956664,36020890,36029577,36044128,36102855,36104798,36127302,36149454,36246798,36261575,36320078,36463253,36497808,36504181,36516791,36527479,36585955,36679240,36710181,36711163,36792224,36863388,36925012,36951423,36986700,37006000,37015780,37037020,37048772,37076977,37084708,37141095,37141351,37147623,37270562,37353553,37373448,37418706,37438901,37529796,37587036,37595044,37618775,37627709,37628356,37633011,37643177,37769683,37816678,37854616,37876169,37882023,37916967,37945205,37956011,38046618,38078988,38156419,38163479,38187775,38342041,38343260,38616807,38684155,38685586,38742608,38763868,38800216,38827910,38971839,38990451,39002896,39170430,39224267,39388773,39439825,39622026,39641047,39689391,39764351,39767240,39861445,39947758,39999861,40047111,40059895,40157897,40218740,40296686,40311734,40394811,40444136,40450896,40518315,40519642,40532590,40538515,40544181,40548176,40794445,40879468,40880684,40962756,41054073,41066030,41094500,41128053,41160390,41169422,41277114,41285028,41325457,41395031,41444517,41455876,41461118,41484196,41544949,41569414,41610030,41642512,41731843,41786940,41840155,41840310,41982483,42008702,42015657,42153159,42157467,42250773,42293395,42312871,42391143,42418282,42501752,42537976,42657255,42722082,42812149,42858085,42868379,42913904,43018573,43071227,43080467,43143544,43173965,43195649,43199841,43209625,43288227,43291020,43342895,43441704,43475585,43545330,43552287,43554683,43598527,43657872,43672989,43685632,43716497,43764383,43797081,43923205,43939287,43975372,44021938,44079745,44100220,44151782,44168533,44235234,44296867,44403378,44405662,44407757,44432938,44509197,44532590,44565573,44643404,44713718,44743245,44754401,44777210,44790235,44797839,44867650,44976553,44984865,44994689,45001527,45035915,45045649,45081826,45239791,45480991,45496807,45506348,45570874,45580834,45617228,45627921,45660647,45681625,45785195,45806217,45815391,45954030,45958676,46066104,46101818,46163499,46187457,46305507,46436331,46438312,46454537,46746431,46875687,46925689,46928519,46947521,47027915,47077681,47096499,47186196,47208377,47436475,47441418,47454664,47488429,47495629,47506500,47506702,47516279,47538482,47594160,47601936,47612895,47613749,47656317,47746596,47894936,47933531,47979744,48141013,48142336,48189714,48205023,48254769,48312221,48362995,48394354,48567737,48568321,48586496,48606199,48629828,48650408,48669920,48730715,48751039,48785116,48926133,49157447,49194522,49240765,49250376,49254477,49328118,49390394,49418431,49483776,49527305,49634747,49650158,49689047,49765986,49766713,49853074,49886380,49922126,49943209,49965240,50018398,50034902,50149004,50180025,50229582,50247184,50250026,50342662,50425282,50599700,50600155,50604580,50636217,50731802,50743963,50758085,50770665,50806806,50863153,50874148,50916230,50948170,50957601,50973124,50997072,51036325,51082655,51116529,51135107,51136492,51138323,51260429,51322589,51347944,51380783,51386671,51501212,51569134,51649472,51682576,51704102,51732512,51842964,51855910,51952459,51971515,52020452,52055728,52095000,52104903,52105477,52122240,52122549,52243184,52244443,52299804,52322226,52338003,52459098,52512767,52517015,52526936,52602303,52607044,52627236,52640044,52646883,52647404,52687302,52692228,52698487,52700611,52701359,52747035,52775101,52848250,52918336,52966310,52970638,53177881,53185705,53192838,53195717,53266090,53311318,53444200,53545420,53569221,53630455,53837115,53855308,53892094,54093424,54123745,54134825,54205344,54339581,54380387,54392878,54518910,54573607,54601725,54669528,54689054,54689546,54744181,54772638,54892901,55008038,55008435,55024038,55053100,55112831,55150394,55263909,55322385,55369338,55394904,55424559,55437196,55449354,55453017,55462084,55467447,55647802,55653051,55839560,55889381,55903233,55951018,56060053,56066508,56136733,56149333,56152509,56256834,56257793,56346173,56378509,56454096,56469204,56505376,56534927,56556859,56597329,56640975,56659891,56707074,56715863,56720506,56730468,56739311,56763136,56883366,56932078,56937137,56951514,56974832,56992496,57009822,57011187,57048222,57070642,57110951,57116054,57140033,57143485,57187235,57309175,57325805,57359882,57416018,57529148,57564621,57574058,57633413,57644833,57651461,57653190,57705954,57833462,57845362,57882838,57883818,57889305,58045840,58093838,58216135,58301744,58318594,58332135,58414603,58452110,58517338,58613780,58653792,58657306,58683693,58711898,58761489,58901908,58969252,58969757,59010272,59121148,59156866,59195525,59408094,59486969,59585296,59596672,59625271,59756157,59820463,59842028,59857165,59865912,59921759,60087437,60160587,60229868,60280223,60321334,60448322,60470853,60473055,60489667,60498894,60572408,60573735,60604786,60624087,60669200,60725196,60741883,60776641,60783131,60856772,60888338,60951293,60957655,60974822,61165026,61300367,61315560,61335444,61351264,61366916,61445165,61660754,61741091,61819600,61842588,61849857,61860615,61887898,61925326,62071675,62098185,62182735,62241010,62261135,62289608,62309650,62323881,62353076,62367139,62381444,62449243,62492870,62542933,62613454,62620909,62621405,62874121,62910887,62928213,63015341,63068117,63106842,63140199,63177684,63183524,63211140,63232464,63234956,63295989,63429709,63524912,63581277,63592923,63612254,63677597,63722364,63739342,63790444,63947533,63985975,64007400,64049561,64114023,64168558,64224574,64236498,64279991,64323175,64356129,64373196,64383136,64388358,64402014,64406930,64458636,64476904,64486442,64487043,64518243,64520206,64524258,64563162,64585083,64671933,64720897,64743772,64751430,64759365,64815128,64825804,64915664,64919847,64929908,64953623,65264146,65280956,65325328,65333583,65399466,65403446,65505422,65590311,65600002,65664177,65666728,65782307,65803180,65900848,65920176,65945133,65981068,66010562,66141358,66160312,66181319,66264650,66285179,66332732,66343950,66415071,66433377,66440613,66505634,66540903,66744264,66756566,66758756,66761473,67017379,67061456,67067038,67086296,67116304,67132275,67147524,67148036,67168047,67301518,67307420,67603328,67773028,67862827,67904416,67931986,67956906,67985872,67992134,68046772,68131045,68133070,68243280,68244028,68276765,68342979,68395591,68398410,68402778,68459540,68466355,68470907,68509820,68510102,68564183,68730719,68756295,68866242,68866983,68919087,68983782,68989161,69016307,69064615,69065290,69113038,69141588,69157586,69203832,69230344,69246598,69374855,69527166,69541236,69573596,69580048,69648881,69753262,69802376,69831813,69851765,69908993,70027163,70113139,70143172,70181609,70362576,70373112,70487346,70545649,70546494,70554116,70597309,70624541,70709494,70807654,70809885,70819185,70859297,70937496,70986413,71067718,71094253,71103787,71168877,71226626,71295527,71317895,71378652,71401759,71445468,71448889,71457111,71488617,71507764,71518374,71523336,71540326,71639789,71647496,71705518,71800709,71844036,71852199,71867001,71873622,71907448,71930608,72036905,72078586,72123354,72168998,72209303,72215451,72234629,72314732,72321301,72374614,72561781,72658710,72668718,72674213,72696294,72776827,72846658,72940412,73092672,73099993,73298258,73329164,73358087,73391334,73406005,73458067,73489289,73539319,73626030,73657922,73976262,74034787,74063138,74112270,74122320,74123565,74131975,74182262,74236977,74254675,74267020,74291058,74373970,74401396,74436891,74458226,74467926,74503993,74551797,74639895,74641905,74656399,74716381,74737734,74772967,74785702,74899587,74989958,74994137,75009902,75030103,75135481,75167101,75260246,75274930,75320992,75321786,75332643,75411044,75417695,75460827,75569730,75577053,75681906,75708804,75933811,75984807,76007044,76086823,76318034,76381335,76433654,76514374,76534973,76579334,76614436,76615014,76653129,76728688,76833574,76893732,76962449,77192514,77357466,77365403,77383604,77489361,77520464,77537102,77593957,77668892,77715982,77768796,77779713,77891393,77938777,77972783,78041845,78119349,78120146,78252980,78277872,78280392,78295228,78309141,78410453,78485100,78488305,78604980,78616502,78649593,78702982,78753762,78767350,78856141,78921564,78964312,78984625,79093261,79126232,79210755,79237173,79305221,79378661,79392140,79417521,79420228,79528340,79555660,79560586,79626880,79667158,79672140,79692053,79758541,79843538,79877986,79895296,79910808,79982834,80031616,80138576,80193490,80322321,80328340,80410044,80414972,80423695,80448020,80492708,80517833,80523354,80651214,80658517,80728168,80769417,80883109,80899730,80900474,80960714,81001413,81100425,81114135,81115809,81124226,81145903,81147906,81148110,81191581,81301290,81378285,81542292,81545705,81634479,81688318,81748726,81754745,81887209,81899273,82010672,82058309,82075832,82186371,82216150,82446635,82471067,82472821,82563456,82567461,82596392,82608949,82647885,82664867,82687487,82749612,82767858,82775675,82827794,82841107,82872695,82930302,82968280,82994764,82998654,82999688,83091017,83096671,83117980,83134256,83157913,83205419,83205869,83279791,83293232,83313449,83397126,83443511,83447687,83474362,83508429,83542760,83592217,83674761,83733630,83758920,83767236,83823790,83841767,83845703,83873263,83899797,83902679,83924008,83937666,83965117,84068103,84167835,84202259,84261356,84292491,84348117,84361370,84443029,84537368,84635548,84687354,84699798,84778154,84861200,84946300,85033405,85128846,85144338,85169724,85187883,85251729,85406006,85423287,85580772,85694238,85701547,85886995,86020168,86054313,86095750,86118101,86122089,86123812,86147218,86276983,86284097,86338650,86416850,86444665,86453411,86474987,86505191,86542081,86558062,86649524,86732097,86805568,86808300,86847515,86920461,87036181,87182624,87213705,87473172,87653303,87735251,87745111,87749094,87749599,87781089,88026530,88044690,88054273,88093652,88205047,88341008,88427834,88534785,88557272,88576954,88584161,88648161,88692174,88725062,88812402,88816550,88823678,88842498,88864366,88899914,88958392,89023107,89052919,89164212,89392669,89406862,89412044,89469788,89492500,89513628,89582109,89646395,89690705,89772809,89800408,89879850,90116022,90166809,90175685,90320916,90401152,90449271,90487860,90512386,90527269,90567781,90572165,90641628,90648643,90650289,90674939,90692495,90732784,90736729,90896364,90909267,90967891,91011487,91023250,91027860,91080104,91082373,91130607,91166851,91179055,91181991,91228171,91269342,91348982,91352285,91356309,91378871,91456801,91457057,91484921,91526262,91635134,91662666,91749696,91991456,92001395,92166491,92176496,92180184,92211783,92258053,92304124,92316406,92322630,92356792,92357749,92372765,92379846,92425967,92568536,92585753,92638034,92687110,92757296,92770792,92809575,92824877,92856350,92911276,92923279,92942232,93230864,93353347,93401066,93410321,93533386,93571035,93590519,93710603,93849932,93855272,93894435,93906648,93909605,93912899,93986494,94018427,94077282,94095584,94135330,94151289,94155006,94179339,94202170,94273664,94299924,94321413,94380980,94399091,94420054,94440241,94562363,94680628,94715017,94748762,94835130,94841208,94864802,94870331,94951703,95053067,95059275,95068030,95101592,95291904,95390694,95396002,95510157,95561977,95618634,95675917,95708256,95719427,95772615,95804395,95823763,95948102,95990691,96159437,96199381,96210063,96279806,96293322,96298972,96307358,96381115,96397821,96427318,96432304,96623160,96626423,96685902,96780303,96803491,96824720,96938326,97061950,97210343,97261608,97278857,97292902,97324001,97361615,97363636,97365992,97375729,97384231,97471432,97511215,97511392,97565144,97609386,97620866,97668473,97721844,97776242,97778566,97793733,97812758,97819023,97836768,97858779,97896991,97974388,98036399,98049856,98050403,98057620,98075489,98163995,98195858,98196080,98425377,98437061,98545966,98551037,98608444,98705452,98758391,98767299,98850153,98938562,98964191,98972153,98975153,98991357,99112531,99132225,99263710,99282170,99331992,99474248,99722670,99730529,99756838,99758397,99817799,99857431,99874659,99908482,99939756,99958464,99998175]
k = 936659

solution = Solution()
print(solution.minmax_gas_dist(stations, k))
