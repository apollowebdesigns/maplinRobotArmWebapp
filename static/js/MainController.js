angular
    .module('app')
    .controller('MainController', MainController);

MainController.$inject = ['$scope']

function MainController($scope) {

    console.log('hit hit')
    $scope.test = 'hello from the test!!!!';
}