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

MainController.$inject = ['$scope', '$http', '$log'];

function MainController($scope, $http, $log) {
    $scope.touched = false;

    $scope.touchStart = function(url) {
        $scope.touched = true;
    }

    $scope.touchEnd = function(url) {
        $scope.touched = false;
    }

    var vm = this;
    vm.isThisMobile = 'is this mobile?';
    vm.isItMobile = Modernizr.touch;
    vm.moveArm = (url) => {
        $log.info('I have been hit!!!');
        $http
            .get("/arm/" + url)
            .then(response => console.log(response));
    }
}