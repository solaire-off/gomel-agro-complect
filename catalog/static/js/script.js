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



	 $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

		if ($navbarBurgers.length > 0) {
			$navbarBurgers.forEach(function ($el) {
				$el.addEventListener('click', function () {

          $jsNavbar = document.getElementById('js-navbar');
          if ($jsNavbar){
            toggleClass($jsNavbar, 'has-open-hamburger');
            if (!hasClass($jsNavbar,'has-shadow')){
              toggleClass($jsNavbar,'is-transparent')
            }
          }

					target = $el.dataset.target;
					$target = document.getElementById(target);

					$el.classList.toggle('is-active');
					$target.classList.toggle('is-active');

				});
			});
		}




  $html         = document.getElementsByTagName('html')[0];
  $popupToggle  = document.querySelectorAll('.js-open-popup');
  $contactPopup = document.getElementById('contact-popup')
  $popupClose   = document.querySelectorAll('.js-close-popup');


  if ($popupToggle &&  $popupClose){

    Array.from($popupToggle).forEach(link => {
      link.addEventListener('click', function(event) {
        $target_id = this.getAttribute('data-target');
        $target = document.getElementById($target_id);
        $target.style.display = 'block';

        toggleClass($html, 'overflow-hidden');

        window.onclick = function(event) {
          if (event.target == $target) {
            $target.style.display = "none";
            toggleClass($html, 'overflow-hidden');
          }
        }

      });
    });

    Array.from($popupClose).forEach(link => {
      link.addEventListener('click', function(event) {
        $target_id = this.getAttribute('data-target');
        $target = document.getElementById($target_id);
        $target.style.display = 'none';

        toggleClass($html, 'overflow-hidden');
      });
    });


  }

  if (document.getElementById('id_phone')){
    $phoneMask = new IMask(document.getElementById('id_phone'), { mask: '+{375} (00) 000-00-00'});
  }


  if (document.getElementById('id_phone_details')){
    $phoneMaskDetails = new IMask(document.getElementById('id_phone_details'), { mask: '+{375} (00) 000-00-00'});
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

  $itemsDetails = document.querySelectorAll('.details .box');

  if ($itemsDetails){
    Array.from($itemsDetails).forEach(detail => {
      detail.addEventListener('click', function(event) {
        toggleClass(this, 'selected')
      });
    });
  }

  $sendForms = document.querySelectorAll('.js-form');

  Array.from($sendForms).forEach($orderForm => {
    $orderForm.addEventListener("submit", function(e){
      e.preventDefault();    //stop form from submitting
      $url       = $orderForm.action;
      $token     = $orderForm.elements["csrfmiddlewaretoken"].value;
      $name      = $orderForm.elements["name"].value;
      $phone     = $orderForm.elements["phone"].value;
      $note      = $orderForm.elements["note"].value;
      $topic     = $orderForm.elements["topic"].value;
      $category  = $orderForm.elements["category"].value;


      if ($itemsDetails){
        $first = true;
        Array.from($itemsDetails).forEach(detail => {
          if (hasClass(detail, 'selected')){
            if ($first){
              $note += "Интерисующие комплектующие: "
              $note += detail.getAttribute('data-title');
              $first = false;
            }
            $note += ', ' + detail.getAttribute('data-title') ;
          }
        });
      }

      // $topic = $orderForm.querySelector('#id_topic') ? $orderForm.querySelector('#id_topic')
      // $topic = document.getElementById('id_topic') ? document.getElementById('id_topic').value : '' ;
      // $category =  document.getElementById('id_category') ? document.getElementById('id_category').value : '' ;

      postAjax($url,{
        name: $name,
        phone: $phone,
        note: $note,
        topic : $topic,
        category : $category,
        csrfmiddlewaretoken: $token
      }, function(data){
        $data = JSON.parse(data);
        if ($data.valid){
          console.log("Successful sending")
          $orderForm.reset();


          successMessage = 'Спасибо! Данные успешно отправлены';
          $orderForm.parentElement.insertAdjacentHTML('afterbegin', '<div class="notification is-link"><button class="delete js-close-popup"></button>' + successMessage  + '</div>');
          $newDeleteButtons = document.querySelector('.delete');

          $newNotification  = $newDeleteButtons.parentElement;

          document.addEventListener('click', function (e) {
            if (hasClass(e.target, 'delete')) {
              $newNotification.remove();
              if (!hasClass($orderForm,'js-no-display')){
                $orderForm.parentNode.parentNode.parentNode.style.display = 'none';
                toggleClass($html, 'overflow-hidden');
              }
            }
          }, false);
        }
        else {
          console.log("Sending error")
        }
      });
    });
  });




  var nav = document.getElementById('js-navbar');

  if (typeof(nav) != 'undefined' && nav != null) {
    window.addEventListener('scroll', function (e) {
      if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight ) {
        nav.classList.remove('is-transparent');
        nav.classList.add('has-shadow');
      } else {
        nav.classList.add('is-transparent');
        nav.classList.remove('has-shadow');
      }
    });
  }




  var arrow = document.getElementById('js-arrow');

  function scrollTo(element, to, duration) {
    if (duration <= 0) return;
    var difference = to - element.scrollTop;
    var perTick = difference / duration * 10;

    setTimeout(function() {
      element.scrollTop = element.scrollTop + perTick;
      if (element.scrollTop === to) return;
      scrollTo(element, to, duration - 10);
    }, 10);
  }


  if (typeof(arrow) != 'undefined' && arrow != null) {
    window.addEventListener('scroll', function (e) {
      if (document.documentElement.scrollTop || document.body.scrollTop > window.innerHeight ) {
        arrow.classList.add('is-up');
      } else {
        arrow.classList.remove('is-up');
      }
    });

    arrow.addEventListener('click', function(e){
      if (hasClass(arrow,'is-up')){
        e.preventDefault();
        window.scroll({ top: 0, left: 0, behavior: 'smooth' });
      }
    });

  }

  var trigger = new ScrollTrigger({
    toggle: {
      visible: 'js-visible',
      hidden: 'js-invisible'
    },
    offset: {
      x: 0,
      y: -550
    },
    addHeight: true,
    // centerVertical: true,
    once: true
  }, document.body, window);

})

