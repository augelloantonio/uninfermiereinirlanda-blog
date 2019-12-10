<script src="http://code.jquery.com/jquery-latest.min.js"></script>
<script>
    var debug = true;

    function mylog(message) {
        if (debug) {
            console.log(message);
        }
    }
    var pulsante = new function() {
        this.countClick = 0;
        this.init = function() {
            mylog('Init-begin');
            this.countClick = 0;
            this.IGTbindEvent();
            mylog('Init-end');
        };
        this.incrementClick = function() {
            this.countClick++;
            $('#counter').html('Numero totale click ' + this.countClick)
            mylog('--- click = ' + this.countClick);
        };
        this.IGTunbindEvent = function() {
            $('#buz').unbind('mousedown mouseup');
            //clearInterval(interval);
            //clearTimeout(testTime);
        };
        this.IGTbindEvent = function() {
            $('#buz').bind('mousedown mouseup', function(event) {
                var evtType = event.type;
                switch (evtType) {
                    case 'mousedown':
                        // incrementClick
                        this.incrementClick();
                        break;
                    case 'mouseup':
                        break;
                    default:
                        break;
                }
            });
        };
    }
    $(document).ready(function() {
        pulsante.init();
    })
</script>
<input type="button" id="buz" value="Premi qui" />
<p id="counter"></p>e() {
    if ($("#input-search").hasClass("hidden-input")) {
        $("#input-search").removeClass("hidden-input");
    } else {
        $("#input-search").addClass("hidden-input");
    }
}


//EmailJs 
function sendMail(contactForm) {
    emailjs.send("gmail", "buyit", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.emailaddress.value,
            "order": contactForm.order.value,
            "enquiry": contactForm.enquiry.value
        })
        .then(
            function (response) {
                var alert = '<div class="alert alert-success" role="alert"> Your message has been sent.You will receive an answer as soon as possible.</div>'
                document.getElementById("email-alert").innerHTML = alert;
            },
            function (error) {
                var alert = '<div class="alert alert-danger" role="alert">Your message was not sent. Please check that all the details are correct.</div>'
                document.getElementById("email-alert").innerHTML = alert;
            }
        );
    return false; // To block from loading a new page
}



var myNamespace = (function () {
    var myVar1, myMethod1;
    myVar1 = 0;
    myMethod1 = function (foo) {
        console.log(foo);
    };
    return {
        myVar2: "foo",
        // A public function utilizing privates
        myMethod2: function (bar) {
            // Increment our private counter
            myVar1++;
            // Call our private method using bar
            myMethod1(bar);
        }
    };
});

console.log(myNamespace.myVar1);
console.log(myNamespace.myVar2);
myNamespace.myMethod1('Method1 call');
myNamespace.myMethod2('Method2 call');
console.log(myNamespace.myVar1);