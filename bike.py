class bikes :
    status:str


    def __init__(self,name,colour,body,mirror,engine) :
        self.naam=name
        self.rang=colour
        self.body=body
        self.mirror=mirror
        self.engine=engine
        self.headlight_status="off"
        self.mainlight_status="off"
        self.fuelmeter_status="off"
    
    
  


    def display(self) :
        print(f"The name of the bike is {self.naam}\nThe colour of the bike is {self.rang}\nThe material of the bike is:{self.body}\nThe no. of mirror in the bike are: {self.mirror}\nThe engine power in cc is: {self.engine}")


    def run(self ) :
        self.status="Running"
        self.headlight_status="on"
        self.mainlight_status="on"
        self.fuelmeter_status="on"
        print("The bike is running ")

    def __kill_engine(self) :
        self.headlight_status="off"
        self.mainlight_status="off"
        self.fuelmeter_status="off"

    def stop(self) :
        self.status="Stopped"
        self.__kill_engine()
        print("The bike is stopped ")


    


BMW = bikes ("BMW21","Black","Metal",2,1213)
BMW.display()
BMW.run()
BMW.stop()
