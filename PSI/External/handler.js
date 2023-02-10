const Full_Name = getComputedStyle(document.documentElement).getPropertyValue("--full-name");
const Split_Name = Full_Name.split(" ");

var Currently_Checked = null;

window.onload = function(){
    
    const Welcome_MSG = document.getElementById("welcome");
    const Profile_Name = document.getElementById("full-name");

    Welcome_MSG.innerHTML = "Welcome to Pulse, " + String(Split_Name[0]) + ".";
    Profile_Name.innerHTML = Full_Name;

}

function Set_Check(T_Category){
    
    const Holder = document.getElementById(T_Category);
    const Checkmark_Holder = Holder.getElementsByClassName("checkmark")[0];

    Checkmark_Holder.style.visibility = 'unset';

    if(Currently_Checked){

        Currently_Checked.style.visibility = 'hidden';

    };

    Currently_Checked = (Currently_Checked == Checkmark_Holder ? null : Checkmark_Holder);

}