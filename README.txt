#NOTE: we are now switching everything over from text files to python dataframes.

This system will not go through time from the perspective of a real user.
for example:
    -When a user logs in, they can click attend on any class no matter when it is, it doesn't matter which order either.
    -A member can choose to pay for a class no matter when it is
    -When a member chooses to pay for a class, the discount they get will depend on their record currently in classes.txt
    -When 


-------------------------------------------------------------------------------------------------------------------------------
users.txt: 
each line will have information about users (seperated by | character)
after a double seperator character || private messages/notifications for the user will be listed each seperated by a |

-------------------------------------------------------------------------------------------------------------------------------
messageBoard.txt
public messages viewable by all members.
each line will contain a message. (messages wont have titles or subjects for simplicity, we can add it later if we have time.)
every time a coach sends a message to members, it will be added as a line on this file.
when a member checks their mailbox, it will show them every message on this file. 
(no sorting and will show all messages not just unread ones for simplicity)

-------------------------------------------------------------------------------------------------------------------------------
classes.txt
We will write out this file ourselves. the only part that will be written by the program is the coaches and members who attend
each line represents one class which members and coaches can attend.
format for each line can be: 

classNumber classDay classMonth expectedCoachAttendee1|expectedCoachAttendee2 expectedMemberAttendee1|expectedMemberAttendee2 coachWhoDidAttend1|coachWhoDidAttend2 memberWhoDidAttend1|memberWhoDidAttend2 memberWhoPayed1|memberWhoPayed2 memberWhoDidNotPay1|memberWhoDidNotPay2

classNumber will a number starting from 0 (first class is 0, second class is 1)
classDay is a number starting from 0 
classMonth is also a number starting from 0 (maybe we can do a few classes in each month number)
all users in the attendees sections will be denoted by their usernames.
expected coach attendees will be seperated by | characters 
same thing goes for expected member attendees, coaches who attended members who attended, members who payed, and members who did not pay.


