(function() {
    var app = angular.module('myApp', []);

    app.controller('MainCtl', function($scope) {
        $scope.sidebarClass = '';

        $scope.setSidebarClass = function(className) {
            if ($scope.sidebarClass == className) {
                $scope.sidebarClass = '';
            } else {
                $scope.sidebarClass = className;
            }
        }
    });

})();