angular
    .module('app')
    .controller('MainController', MainController)
    .directive('myTouchstart', [function() {
        return function(scope, element, attr) {

            element.on('touchstart', function(event) {
                scope.$apply(function() { 
                    scope.$eval(attr.myTouchstart); 
                });
            });
        };
    }]).directive('myTouchend', [function() {
        return function(scope, element, attr) {

            element.on('touchend', function(event) {
                scope.$apply(function() { 
                    scope.$eval(attr.myTouchend); 
                });
            });
        };
    }]);

MainController.$inject = ['$http', '$log'];

function MainController($http, $log) {
    var vm = this;
    vm.touched = false;

    vm.touchStart = function() {
        vm.touched = true;
    }

    vm.touchEnd = function() {
        vm.touched = false;
    }

    vm.test = 'from main controller';
    vm.moveArm = (url) => {
        $log.info('I have been hit!!!');
        $http
            .get("/arm/" + url)
            .then(response => console.log(response));
    }
}