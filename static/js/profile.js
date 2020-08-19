const profilePanel = $('#account-profile-panel');
const ordersPanel = $('#account-orders-panel');
const logOutPanel = $('#account-profile-logout-panel');

//click function to handle the active class for profile navigation
$('li').click(function() {
    $('.active').removeClass('active');
    $(this).addClass('active');
});

//onclick events to handle which panel is showing per click | default is My account /contact information
$('#account-profile').click(function(){
    profilePanel.show();
    ordersPanel.hide();
    logOutPanel.hide();
    return false;
});

$('#account-orders').click(function(){
    profilePanel.hide();
    logOutPanel.hide();
    ordersPanel.show();
    return false;
});

$('#account-logout').click(function(){
    profilePanel.hide();
    ordersPanel.hide();
    logOutPanel.show();
    return false;
});
