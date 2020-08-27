//Boostrap toasts
$('.toast').toast('show');

//Product management Delete confirmation poopup for admin removing products
const deleteButton = $('#delete-button');
const deletePopup = $('.overlay-delete');
const popupText = $('#delete-popup');  

// Mobile Side nav
const burgerIcon = $('.burger-button');
const mobileNav = $('.mobile-nav');
const mobileNavBg = $('.nav-background');

// Product management on click handler
deleteButton.click(function(){
    deletePopup.show();
    deletePopup.addClass('overlay-show');
    popupText.show();
    return false;
});

deletePopup.click(function(){
    deletePopup.hide();
    deletePopup.removeClass('overlay-show');
    popupText.hide();
});


// Mobile Side nav handler

burgerIcon.click(function(){
    mobileNavBg.show();
    mobileNavBg.addClass('overlay-nav');
    mobileNav.addClass('transition');
    return false;
});

mobileNavBg.click(function(){
    mobileNavBg.removeClass('overlay-nav');
    mobileNav.removeClass('transition');
})
