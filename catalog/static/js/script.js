document.addEventListener("DOMContentLoaded", function() {

    function hasClass(elem, className) {
        return new RegExp(' ' + className + ' ').test(' ' + elem.className + ' ');

    }

    function addClass(elem, className) {
        if (!hasClass(elem, className)) {
            elem.className += ' ' + className;

        }

    }

    function removeClass(elem, className) {
        var newClass = ' ' + elem.className.replace( /[\t\r\n]/g, ' ' ) + ' ';
        if (hasClass(elem, className)) {
            while (newClass.indexOf(' ' + className + ' ') >= 0 ) {
                newClass = newClass.replace(' ' + className + ' ', ' ');

            }
            elem.className = newClass.replace(/^\s+|\s+$/g, '');

        }

    }
    function toggleClass(elem, className) {
        var newClass = ' ' + elem.className.replace( /[\t\r\n]/g, " "  ) + ' ';
        if (hasClass(elem, className)) {
            while (newClass.indexOf(" " + className + " ") >= 0 ) {
                newClass = newClass.replace( " " + className + " " , " "  );

            }
            elem.className = newClass.replace(/^\s+|\s+$/g, '');

        } else {
            elem.className += ' ' + className;

        }

    }

    $html         = document.getElementsByTagName('html')[0];
    $popupToggle  = document.querySelector('.js-open-popup');
    $contactPopup = document.getElementById('contact-popup')
    $popupClose   = document.querySelector('.js-close-popup');


    if ($popupToggle &&  $popupClose){
        $popupToggle.addEventListener('click', function() {
            $contactPopup.style.display = 'block';
            toggleClass($html, 'overflow-hidden');

        });

        $popupClose.addEventListener('click', function() {
            $contactPopup.style.display = 'none';
            toggleClass($html, 'overflow-hidden');
        });


        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == $contactPopup) {
                $contactPopup.style.display = "none";
                toggleClass($html, 'overflow-hidden');
            }
        }

        $phoneMask = new IMask(document.getElementById('id_phone'), { mask: '+{375} (00) 000-00-00'});

    }

    function postAjax(url, data, success) {
        var params = typeof data == 'string' ? data : Object.keys(data).map(
            function(k){ return encodeURIComponent(k) + '=' + encodeURIComponent(data[k]) }
        ).join('&');

        var xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");
        xhr.open('POST', url);
        xhr.onreadystatechange = function() {
            if (xhr.readyState>3 && xhr.status==200) { success(xhr.responseText); }
        };
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send(params);
        return xhr;
    }

    // example request
    // postAjax('http://foo.bar/', 'p1=1&p2=Hello+World', function(data){ console.log(data); });

    // example request with data object
    // postAjax('http://foo.bar/', { p1: 1, p2: 'Hello World' }, function(data){ console.log(data); });


    $orderForm = document.getElementById('order-form');

    if ($orderForm){
        $orderForm.addEventListener("submit", function(e){
            e.preventDefault();    //stop form from submitting
            $url   = $orderForm.action;
            $token = $orderForm.elements["csrfmiddlewaretoken"].value;
            $name  = $orderForm.elements["name"].value;
            $phone = $orderForm.elements["phone"].value;
            $note  = $orderForm.elements["note"].value;
            // get value in hidden field
            $item  = document.getElementById("item_id").value;
            postAjax($url,{
                name: $name,
                phone: $phone,
                note: $note,
                item : $item,
                csrfmiddlewaretoken: $token
            }, function(data){
                $data = JSON.parse(data);
                if ($data.valid){
                    console.log("Successful sending")

                    $orderForm.reset();
                    // $contactPopup.style.display = 'none';


                    successMessage = 'Спасибо! Данные успешно отправлены';
                    $orderForm.parentElement.insertAdjacentHTML('afterbegin', '<div class="notification is-link"><button class="delete js-close-popup"></button>' + successMessage  + '</div>');
                    $newDeleteButtons = document.querySelector('.delete');



                    $newNotification  = $newDeleteButtons.parentElement;

                    // $newDeleteButtons.addEventListener('click', function() {
                    //     $newNotification.remove();
                    //     $contactPopup.style.display = 'none';
                    //     toggleClass($html, 'overflow-hidden');
                    // });

                    document.addEventListener('click', function (e) {
                        if (hasClass(e.target, 'delete')) {
                            $newNotification.remove();
                            $contactPopup.style.display = 'none';
                            toggleClass($html, 'overflow-hidden');
                        }
                    }, false);
                }
                else {
                    console.log("Sending error")
                }
            });
        });
    }
	window.addEventListener('scroll', function (e) {
        var nav = document.getElementById('js-navbar');
        if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight) {
                nav.classList.remove('is-transparent');
            } else {
                nav.classList.add('is-transparent');
            }
    });

	var trigger = new ScrollTrigger({
		  toggle: {
			visible: 'js-visible',
			hidden: 'js-invisible'
		  },
		  offset: {
			x: 0,
			y: -350
		  },
		  addHeight: true,
		  once: true
		}, document.body, window);

})

