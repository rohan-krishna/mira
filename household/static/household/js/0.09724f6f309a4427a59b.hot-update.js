webpackHotUpdate(0,{

/***/ 21:
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var _react = __webpack_require__(6);

var _react2 = _interopRequireDefault(_react);

var _reactDom = __webpack_require__(22);

var _reactDom2 = _interopRequireDefault(_reactDom);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var App = function App() {
    return _react2.default.createElement(
        'h1',
        null,
        'Hello World!'
    );
};

window.onload = function () {
    _reactDom2.default.render(_react2.default.createElement(App, null), document.getElementById("#reactApp"));
};

module.hot.accept();

/***/ })

})