                tuong = webdriver.Chrome(executable_path=r"D:\python\chromedriver.exe")
                tuong.set_window_size(1000,1000)
                tuong.get("https://www.facebook.com/campaign/landing.php?campaign_id=1661697991&extra_1=s%7Cc%7C432702091386%7Cb%7C%C4%91%C4%83ng%20ky%CC%81%20facebook%7C&placement=&creative=432702091386&keyword=%C4%91%C4%83ng%20ky%CC%81%20facebook&partner_id=googlesem&extra_2=campaignid%3D1661697991%26adgroupid%3D65157403438%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-369935470948%26loc_physical_ms%3D9047170%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMInK-f1ouz9gIV0m4qCh3s3Q27EAAYASAAEgLRovD_BwE") 
                tuong.find_element_by_name("lastname").send_keys(" trần")
                tuong.find_element_by_name("firstname").send_keys("tường")
                tuong.find_element_by_name("reg_email__").send_keys("thetuongyt@gmail.com")
                sleep(2)
                tuong.find_element_by_name("reg_email_confirmation__").send_keys("thetuongyt@gmail.com")
                file_object = open("password.txt")
                data = file_object.read()
                tuong.find_element_by_id("password_step_input").send_keys(data)
                tuong.find_element_by_name("birthday_day").click()
                tuong.find_element_by_name("birthday_month").click()
                tuong.find_element_by_name("birthday_year").click()
                tuong.find_element_by_name("sex").click()
                sleep(2)
                tuong.find_element_by_name("websubmit").click()
                tuong.find_element_by_name("websubmit").click()
                tuong.find_element_by_name("birthday_age").send_keys("22")
                tuong.find_element_by_name("websubmit").click()
                if sleep(time) == bot.say("exit"):
                    bot.runAndWait()



                    tuong = uc.Chrome()
                tuong.set_window_size(1000,1000)
                tuong.get("http://gmail.com")
                tuong.find_element_by_id("identifierId").send_keys("lol00sever@gmail.com")   
                tuong.find_element_by_xpath("//*[@id='identifierNext']").click()
                tuong.find_element_by_id("password").send_keys("12343211234321")
                tuong.find_element_by_name("passwordNext").click()
                sleep(10)