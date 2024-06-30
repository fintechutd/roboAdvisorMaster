/*
Author: Calvin Xie
Date: 03/05/2024
Purpose of program:
This program will calculate a numerical risk value depending on a users response. 
This will eventually be translated into frontend buttons, etc.


g++ -o a retirement_goal.cpp
*/


/*
goal questions:

Retirement - 
What age are you now?
When do you plan to retire?
How much will you need in retirement to pay for your cost of living?
Will you take care of only yourself or a spouse or other dependents?
How will taxes impact your retirement income?
Do you have social security to assist with the retirement cost of living?
How much are you able to invest now?
How much are you able to invest on a monthly basis?
*/

// the Goals class

#include <iostream>

class Goal
{
    private:
        std::string goalName;
        int goalTargetYear;
        long goalTargetValue;
        long goalInitialContribution;
        double monthlyContribution;

    public:
        // constructor where initial/monthly contributions are optional
        Goal(
            std::string goalName, 
            int goalTargetYear, 
            long goalTargetValue, 
            double goalInitialContribution = 0, 
            double monthlyContribution = 0
            )
        {
            this->goalName = goalName; 
            this->goalTargetYear = goalTargetYear;
            this->goalTargetValue = goalTargetValue;
            this->goalInitialContribution = goalInitialContribution;
            this->monthlyContribution = monthlyContribution;
        } 

        // setters
        void setGoalName(std::string n){ this->goalName = n; }
        void setTargetYear(int n){ this->goalTargetYear = n; }
        void setTargetValue(long n){ this->goalTargetValue = n; }
        void setInitialContribution(double n){ this->goalInitialContribution = n; }
        void setMonthlyContribution(double n){ this->monthlyContribution = n; }


        // getters
        std::string getGoalName(){ return this->goalName; }
        int getTargetYear(){ return this->goalTargetYear; }
        long getTargetValue(){ return this->goalTargetValue; }
        double getInitialContribution(){ return this->goalInitialContribution; }
        double getMonthlyContribution(){ return this->monthlyContribution; }
};

int main()
{
    Goal g("Retirement", 2060, 3000000);
    std::cout<<g.getInitialContribution()<<std::endl;
    return 0;
}

