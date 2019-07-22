#Version_Start:Head_Line=Greeting
    Put "Hello There Welcome to Worl cup 2019 here in England. The creator of this beautiful Game"
#Version_End:Greeting

Data _Null_;
    %put Nothing to Say;
Run;
#Version_Start:Team_List=No
    Put India
        Australia
        Pakistan
        Sri Lanka
        England
        New Zeland
        South Africa
        Bangladesh
        Afganistan
        West Indies;
#Version_End:Team_List


Data _Null_;
    %put Nothing to Say;
Run;

Data _Null_;
    %put Nothing to Say;
Run;

#Version_Start:Expected_Winner=Yes
    Put "We are all Excpecting India to Win"
#Version_End:Greeting


Data _Null_;
    %put Nothing to Say;
Run;

Data _Null_;
    %put Nothing to Say;
Run;

#Version_Start:Best_Batsman=Yes
    Put "VIRAT KOHLI......"
#Version_End:Best_Batsman


#Best_Batsman=Yes
{{{}
    Put"VIRAT KOHLI......"
}

#Version_Start:Best_Batsman=yes
{{Testing
    Put"VIRAT KOHLI......"
    
}}


}