from servo import Servo, servo2040
from transition import Transition
from time import sleep, ticks_us

class Super_servo(Servo):
    __current_angle = 0
    __transition = "ease_in_sine"
    __duration = 0.5 # Transition Duration in seconds
    __target_angle = 0
    __current_time = 0
    __start_value = 0

    # def __init__(self, value):
    #     self.servo = Servo

    @property
    def current_angle(self):
        """ Gets the current angle """
        return self.__current_angle

    @current_angle.setter
    def current_angle(self, value):
        """ Sets the current angle """
        self.__current_angle = value
    
    def tick_start(self):
        self.__tick_start_time = ticks_us()
    
    def tick(self):
        self.__current_time = ticks_us()
        elapsed_time = self.elapsed_time
        if elapsed_time >= self.__duration:
            return True
        
        cur_angle = self.__current_angle

        if self.__transition == 'ease_in_sine':
            cur_angle = Transition().ease_in_sine(current_time=self.elapsed_time, 
                                                  start_value=self.__start_value, 
                                                  change_in_value=self.__start_value-self.__target_angle,
                                                  duration=self.__duration, 
                                                  start_time=ticks_us, target_angle=self.__target_angle)
            self.value = int(cur_angle)

class Limb():
    __name = "no_name"
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

def wiggle(this_servo):
    for _ in range (3):
        this_servo.value(20)
        sleep(0.25)
        this_servo.value(-20)
        sleep(0.25)
    
class Bunny():
    __name = "no_name"
    legs = []
    
    # Setup the Head and turn it to the mid point
    HEAD = Servo(servo2040.SERVO_1)
#     HEAD.to_mid()
    
    NECK = Servo(servo2040.SERVO_2)
#     NECK.to_mid()
    
    FRONT_RIGHT_FOOT = Servo(servo2040.SERVO_3)
    FRONT_LEFT_FOOT = Servo(servo2040.SERVO_4)
    FRONT_LEFT_LEG = Servo(servo2040.SERVO_6)
    FRONT_RIGHT_LEG = Servo(servo2040.SERVO_12) 
    TAIL = Servo(servo2040.SERVO_7)
    BACK_RIGHT_LEG = Servo(servo2040.SERVO_8)
    BACK_RIGHT_FOOT = Servo(servo2040.SERVO_9)
    BACK_LEFT_LEG = Servo(servo2040.SERVO_10)
    BACK_LEFT_FOOT = Servo(servo2040.SERVO_11)
    
    def __init__(self):
        print('*** RoboBunny ONLINE ***')
    
    

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        print("Hello, my name is", self.__name)
        
    def nod(self):
        self.NECK.value(0)
        sleep(0.5)
        self.NECK.value(-50)
        sleep(0.5)
        self.NECK.value(0)
        sleep(0.25)
    
    def wag_tail(self, times):
        for n in range(times):
            self.TAIL.value(50)
            sleep(0.25)
            self.TAIL.value(-50)
            sleep(0.25)
        self.TAIL.to_mid()
    
    def look_left(self):
        self.HEAD.value(50)
        
    def look_right(self):
        self.HEAD.value(-50)
        
    def look_ahead(self):
        self.HEAD.value(0)

    def stand_up(self):
        leg_value = 0
        foot_value = 0
        
        self.FRONT_LEFT_FOOT.value(foot_value)
        self.FRONT_RIGHT_FOOT.value(foot_value)
        self.BACK_LEFT_FOOT.value(foot_value)
        self.BACK_RIGHT_FOOT.value(foot_value)
    
        self.FRONT_LEFT_LEG.value(leg_value)
        self.FRONT_RIGHT_LEG.value(-leg_value)
        self.BACK_LEFT_LEG.value(-leg_value)
        self.BACK_RIGHT_LEG.value(leg_value)
        sleep(1)

    def stand(self):
        amount = 50
        foot_value = 0
        print(self.FRONT_LEFT_FOOT.value())
        print(self.FRONT_LEFT_LEG.value())
        while self.FRONT_LEFT_FOOT.value()!= foot_value and \
              self.FRONT_RIGHT_FOOT.value()!= foot_value and \
              self.BACK_LEFT_FOOT.value()!= foot_value and \
              self.BACK_RIGHT_FOOT.value()!= foot_value and \
              self.FRONT_LEFT_LEG.value()!= amount and \
              self.FRONT_RIGHTT_LEG.value()!= amount and \
              self.BACK_LEFT_LEG.value()!= amount and \
              self.BACK_RIGHT_LEG.value()!= amount:
                            
            self.FRONT_LEFT_LEG.value(i)
            self.FRONT_RIGHT_LEG.value(-i)
            self.BACK_LEFT_LEG.value(-i)
            self.BACK_RIGHT_LEG.value(i)
            print(self.FRONT_LEFT_FOOT.value())
            
#             amount = 0
            if self.FRONT_LEFT_FOOT.value() <= foot_value:
                self.FRONT_LEFT_FOOT.value(self.FRONT_LEFT_FOOT.value()-1)
            elif self.FRONT_LEFT_FOOT.value() > foot_value:
                self.FRONT_LEFT_FOOT.value(self.FRONT_LEFT_FOOT.value()+1)
                
            if self.FRONT_RIGHT_FOOT.value() <= foot_value:
                self.FRONT_RIGHT_FOOT.value(self.FRONT_RIGHT_FOOT.value()-1)
            elif self.FRONT_RIGHT_FOOT.value > foot_value:
                self.FRONT_RIGHT_FOOT.value(self.FRONT_RIGHT_FOOT.value()-1)
            
            if self.BACK_LEFT_FOOT.value() <= foot_value:
                self.BACK_LEFT_FOOT.value(self.BACK_LEFT_FOOT.value()+1)
            elif self.BACK_LEFT_FOOT.value() > foot_value:
                self.BACK_LEFT_FOOT.value(self.BACK_LEFT_FOOT.value()-1)
                
            if self.BACK_RIGHT_FOOT.value() <= foot_value:
                self.BACK_RIGHT_FOOT.value(self.BACK_RIGHT_FOOT.value()+1)
            elif self.BACK_RIGHT_FOOT.value() > foot_value:
                self.BACK_RIGHT_FOOT.value(self.BACK_RIGHT_FOOT.value()-1)
            sleep(0.1)
    
    def sit(self):
        for i in range(50, 90, 1):
            self.FRONT_LEFT_LEG.value(i)
            self.FRONT_RIGHT_LEG.value(-i)
            self.BACK_LEFT_LEG.value(-i)
            self.BACK_RIGHT_LEG.value(i)
            
            self.FRONT_LEFT_FOOT.value(i)
            self.FRONT_RIGHT_FOOT.value(-i)
            self.BACK_LEFT_FOOT.value(i)
            self.BACK_RIGHT_FOOT.value(-i)
            sleep(0.1)

    def hop(self):

        hopped = False
        while not hopped:
            self.FRONT_LEFT_LEG.value(0)
            hopped = True
           
