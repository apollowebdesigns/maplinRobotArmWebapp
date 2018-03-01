angular
    .module('app')
    .directive('mainDirective', MainDirective);

function mainDirective() {
    var directive = {
        // link: link,
        template: '<div>Hello from the directive</div>',
        restrict: 'EA'
    };
    return directive;

    // function link(scope, element, attrs) {
    //   /* */
    // }
}