jQuery(document).ready(function($) {
    const location = window.location.pathname;
    const activeLink = $(`a[href="${location}"]`);
    activeLink.children().addClass("active");
    console.log(location)
});