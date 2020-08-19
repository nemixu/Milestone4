const profilePanel = $('#account-profile-panel');
const ordersPanel = $('#account-orders-panel');
const logOutPanel = $('#account-profile-logout-panel');

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
