/**
 * @license
 * Lodash (Custom Build) lodash.com/license | Underscore.js 1.8.3 underscorejs.org/LICENSE
 * Build: `lodash include="debounce,throttle"`
 */
;(function(){function t(){}function e(t){return null==t?t===l?d:y:I&&I in Object(t)?n(t):r(t)}function n(t){var e=$.call(t,I),n=t[I];try{t[I]=l;var r=true}catch(t){}var o=_.call(t);return r&&(e?t[I]=n:delete t[I]),o}function r(t){return _.call(t)}function o(t,e,n){function r(e){var n=d,r=g;return d=g=l,x=e,v=t.apply(r,n)}function o(t){return x=t,O=setTimeout(c,e),T?r(t):v}function i(t){var n=t-h,r=t-x,o=e-n;return w?k(o,j-r):o}function f(t){var n=t-h,r=t-x;return h===l||n>=e||n<0||w&&r>=j}function c(){
var t=D();return f(t)?p(t):(O=setTimeout(c,i(t)),l)}function p(t){return O=l,S&&d?r(t):(d=g=l,v)}function s(){O!==l&&clearTimeout(O),x=0,d=h=g=O=l}function y(){return O===l?v:p(D())}function m(){var t=D(),n=f(t);if(d=arguments,g=this,h=t,n){if(O===l)return o(h);if(w)return O=setTimeout(c,e),r(h)}return O===l&&(O=setTimeout(c,e)),v}var d,g,j,v,O,h,x=0,T=false,w=false,S=true;if(typeof t!="function")throw new TypeError(b);return e=a(e)||0,u(n)&&(T=!!n.leading,w="maxWait"in n,j=w?M(a(n.maxWait)||0,e):j,S="trailing"in n?!!n.trailing:S),
m.cancel=s,m.flush=y,m}function i(t,e,n){var r=true,i=true;if(typeof t!="function")throw new TypeError(b);return u(n)&&(r="leading"in n?!!n.leading:r,i="trailing"in n?!!n.trailing:i),o(t,e,{leading:r,maxWait:e,trailing:i})}function u(t){var e=typeof t;return null!=t&&("object"==e||"function"==e)}function f(t){return null!=t&&typeof t=="object"}function c(t){return typeof t=="symbol"||f(t)&&e(t)==m}function a(t){if(typeof t=="number")return t;if(c(t))return s;if(u(t)){var e=typeof t.valueOf=="function"?t.valueOf():t;
t=u(e)?e+"":e}if(typeof t!="string")return 0===t?t:+t;t=t.replace(g,"");var n=v.test(t);return n||O.test(t)?h(t.slice(2),n?2:8):j.test(t)?s:+t}var l,p="4.17.5",b="Expected a function",s=NaN,y="[object Null]",m="[object Symbol]",d="[object Undefined]",g=/^\s+|\s+$/g,j=/^[-+]0x[0-9a-f]+$/i,v=/^0b[01]+$/i,O=/^0o[0-7]+$/i,h=parseInt,x=typeof global=="object"&&global&&global.Object===Object&&global,T=typeof self=="object"&&self&&self.Object===Object&&self,w=x||T||Function("return this")(),S=typeof exports=="object"&&exports&&!exports.nodeType&&exports,N=S&&typeof module=="object"&&module&&!module.nodeType&&module,E=Object.prototype,$=E.hasOwnProperty,_=E.toString,W=w.Symbol,I=W?W.toStringTag:l,M=Math.max,k=Math.min,D=function(){
return w.Date.now()};t.debounce=o,t.throttle=i,t.isObject=u,t.isObjectLike=f,t.isSymbol=c,t.now=D,t.toNumber=a,t.VERSION=p,typeof define=="function"&&typeof define.amd=="object"&&define.amd?(w._=t, define(function(){return t})):N?((N.exports=t)._=t,S._=t):w._=t}).call(this);/*jshint esversion: 6 */

const toggle = {
  // standard open/close buttons, usually closes all other menus before opening its menu
  any: '[data-reveal=toggle]',
  search: '[data-reveal=search]',

  // mobile hamburger toggle
  mobileNav: $('#int-nav-toggle_mobile'),

  // 1st & 2nd nav toggles
  nav: $('.int-nav-1st-toggle, .int-nav-2nd-toggle'),

  // nav search
  navSearch: $('#int-nav-search-toggle_desk'),
};

// the menus and trays handled by the buttons in toggle, above
const menu = {
  // all menus that should close with a body-click or ESC-press
  any: '[data-reveal=menu]',

  // mobile hamburger menu
  mobileNav: $('#int-nav-menu_mobile'),

  // 1st & 2nd nav menus
  nav: $('.int-nav-1st-menu, .int-nav-2nd-menu'),
};

// open/close, expand/collapse
const reveal = {

  // update a toggle's aria-expanded attribute
  attrUpdate(toggle, isOpen) {
    // if the toggle's menu is currently closed
    if (!isOpen) {
      // set it to open
      toggle.attr('aria-expanded', true);
    } else {
      // otherwise, set it to closed
      toggle.attr('aria-expanded', false);
    }
  },

  // open/close the dropdown/menu
  move(
    // the target button clicked
    toggle = reveal.findButton(event.target),
    // its target menu as defined by its aria-controls attribute
    menu = $('#' + toggle.attr('aria-controls')),
    // whether to use jQuery's slide or fade effect
    effect = 'slide') {

    // is the dropdown/menu already open?
    const isOpen = toggle.attr('aria-expanded') === 'true';

    // jQuery slideToggle or fadeToggle the target menu
    if (effect === 'slide') {
      menu.slideToggle(200);
    } else if (effect === 'fade') {
      menu.fadeToggle(200);
    }

    // update the target toggle's aria-expanded attribute
    reveal.attrUpdate(toggle, isOpen);
  },

  // reset an element to its onload state
  reset(element) {
    if (element) {
      element.each(function() {
        // if the element is a toggle
        if ($(this).is(toggle.any)) {
          // reset its aria-expanded attribute
          $(this).attr('aria-expanded', false);
        // or, if it's a menu
        } else if ($(this).is(menu.any)) {
          // slide it up
          $(this).slideUp(200, function() {
            // and reset its display (artifact from jQuery slide)
            $(this).css('display', '');
          });
        } else if ($(this).is(toggle.search)) {
          $(this).fadeOut(200);
        }
      });
    }
  },

  // HELPERS

  // find enclosing button if a child element is clicked
  findButton(element) {
    // if the clicked element is a toggle
    if ($(element).is(toggle.any)) {
      // that's great
      return $(element);
    // otherwise
    } else {
      // find it's closest parent that's a toggle
      return $(element).closest(toggle.any);
    }
  },

  // similar to above, find any enclosing menu if a child element is clicked
  parentIsMenu(element) {
    return $(element).parents(menu.any).length > 0;
  },

  // SPECIFIC ELEMENTS

  // Press Express in the global nav
  hamburger(event) {
    // open/close the menu
    reveal.move();
    // freeze/unfreeze the body so it doesn't scroll behind the mobile nav
    // $('body').toggleClass('fixed');
  },
};

// home marquee
const marquee = {
  region: $('#int-marquee'),
  anyArticle: '.int-marquee-article',
  anyArt: '.int-marquee-spin-link',
  article: $('.int-marquee-article'),
  art: $('.int-marquee-spin-link'),
  more: $('.int-marquee-more-link'),


  // show artwork for hovered article
  reveal() {
    // the article hovered
    let article = marquee.findArticle(event.target),
        // its target artwork as defined by its aria-controls attribute
        art = $('#' + article.attr('aria-controls'));

    // fade out all sibling artwork
    art.siblings().css('opacity', '0')
      .css('visibility', 'hidden')
      .attr('aria-hidden', true);
    // fade in the live one
    art.css('opacity', '1')
      .css('visibility', 'visible')
      .attr('aria-hidden', false);
  },

  // highlight titles for hovered art
  hilite() {
    // the art hovered
    let art = marquee.findArt(event.target),
        // its target article as defined by its aria-controls attribute
        article = $('#' + art.attr('aria-controls'));

    // add the on class
    article.toggleClass('on');
  },

  // reset the marquee
  reset() {
    $('#int-marquee-spin-link_2, #int-marquee-spin-link_3, #int-marquee-spin-link_4')
      .css('opacity', '0')
      .css('visibility', 'hidden')
      .attr('aria-hidden', true);

    $('#int-marquee-spin-link_1')
      .css('opacity', '1')
      .css('visibility', 'visible')
      .attr('aria-hidden', false);
  },

  // HELPERS

  // find enclosing article if a child element is hovered
  findArticle(element) {
    // if the clicked element is an article
    if ($(element).is(marquee.anyArticle)) {
      // that's great
      return $(element);
    // otherwise
    } else {
      // find it's closest parent that's an article
      return $(element).closest(marquee.anyArticle);
    }
  },

  // find enclosing article if a child element is hovered
  findArt(element) {
    // if the clicked element is an article
    if ($(element).is(marquee.anyArt)) {
      // that's great
      return $(element);
    // otherwise
    } else {
      // find it's closest parent that's an article
      return $(element).closest(marquee.anyArt);
    }
  },
};

// search forms
const search = {
  navForm: $('#int-nav-search-form_desk'),
  navInput: $('#int-nav-search-input_desk'),
};

// media queries
const responsive = {
  // mobileUp: window.matchMedia('(min-width: 576px)'),
  // tabletUp: window.matchMedia('(min-width: 768px)'),
  deskUp: window.matchMedia('(min-width: 1000px)'),

  deskQuery(e) {
    if (e.matches) {
      // console.log('desk yup!');

      reveal.reset($(toggle.any));
      reveal.reset($(menu.any));

      reveal.reset(search.navForm);

      $('body').removeClass('fixed');

    } else {
      // console.log('desk noop!');

      reveal.reset($(toggle.any));
      reveal.reset($(menu.any));

      reveal.reset(search.navForm);

      $('body').removeClass('fixed');

    }
  }
};

$(document).ready(function() {

  // responsiveness
  // responsive.mobileUp.addListener(responsive.mobileQuery);
  // responsive.mobileQuery(responsive.mobileUp);
  // responsive.tabletUp.addListener(responsive.tabletQuery);
  // responsive.tabletQuery(responsive.tabletUp);
  responsive.deskUp.addListener(responsive.deskQuery);
  responsive.deskQuery(responsive.deskUp);

  // toggle listeners

  toggle.mobileNav.click(function() {
    reveal.hamburger();
  });

  toggle.nav.click(function() {
    const button = reveal.findButton(event.target),
          isOpen = button.attr('aria-expanded') === 'true';

    if (!isOpen) {
      reveal.reset(toggle.nav);
      reveal.reset(menu.nav);
    }

    reveal.move();
  });

  // toggle.navHover.hover(function() {
  //   console.log('got this far');
  //   reveal.hover();
  // });

  // toggle.navHover.hover(
  //   function() {
  //     // $('.header-subnav').slideUp(200);
  //     $(this).children('[data-reveal=menu]').slideToggle(200);
  //   // }, function() {
  //   //   $(this).children('[data-reveal=menu]').slideToggle(200);
  //   }
  // );

  // $('.int-nav-1st-link_desk > a, .int-nav-2nd-link_desk > a, .int-nav-1st-link_desk button, .int-nav-2nd-link_desk button').focus(function() {
  //   menu.nav.slideUp(200);
  //   $(this).next('[data-reveal=menu]').slideToggle(200);
  // });

  $('#modal_login').focus(function() {
    $('[for=modal_login]').css('outline-style', 'auto');
  }).blur(function() {
    $('[for=modal_login]').css('outline-style', '');
  }).keypress(function(e){
    if((e.keyCode ? e.keyCode : e.which) == 13){
        $(this).trigger('click');
    }
  });

  $('#modal_login_mobile').focus(function() {
    $('[for=modal_login_mobile]').css('outline-style', 'auto');
  }).blur(function() {
    $('[for=modal_login_mobile]').css('outline-style', '');
  }).keypress(function(e){
    if((e.keyCode ? e.keyCode : e.which) == 13){
        $(this).trigger('click');
    }
  });

  toggle.navSearch.click(function() {
    reveal.reset($(toggle.nav));
    reveal.reset($(menu.nav));

    reveal.move(undefined, undefined, 'fade');
    search.navInput.focus();
  });

  // marquee

  if (marquee.region.length) {
    marquee.article.on('mouseenter focus', function() {
      marquee.reveal(event.target);
    });

    marquee.art.hover(function() {
      marquee.hilite(event.target);
    });

    marquee.region.hover(function() {}, function() {
      marquee.reset();
    });

    marquee.more.hover(function() {
      marquee.reset();
    }, function() {});
  }

  // resets

  $('body').click(function(event) {
    var button = reveal.findButton(event.target);

    if (!(button.is(toggle.any) || reveal.parentIsMenu(event.target) || $(event.target).is('input[type=search]'))) {
      reveal.reset($(toggle.any));
      reveal.reset($(menu.any));

      reveal.reset(search.navForm);

      $('body').removeClass('fixed');
    }
  });

  $(document).on('keyup', function(event) {
    var ESCAPE_KEY_CODE = 27;

    if(event.keyCode === ESCAPE_KEY_CODE) {
      $(event.target).blur();
      reveal.reset($(toggle.any));
      reveal.reset($(menu.any));

      reveal.reset(search.navForm);

      $('body').removeClass('fixed');
    }
  });
});
