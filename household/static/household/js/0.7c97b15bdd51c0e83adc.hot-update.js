webpackHotUpdate(0,[
/* 0 */,
/* 1 */,
/* 2 */
false,
/* 3 */
false,
/* 4 */
false,
/* 5 */
false,
/* 6 */
false,
/* 7 */
false,
/* 8 */,
/* 9 */,
/* 10 */
false,
/* 11 */
false,
/* 12 */,
/* 13 */
false,
/* 14 */
false,
/* 15 */
false,
/* 16 */
false,
/* 17 */
false,
/* 18 */,
/* 19 */
false,
/* 20 */,
/* 21 */
false,
/* 22 */,
/* 23 */,
/* 24 */
false,
/* 25 */
false,
/* 26 */
false,
/* 27 */
false,
/* 28 */,
/* 29 */
false,
/* 30 */
false,
/* 31 */
false,
/* 32 */
false,
/* 33 */
false,
/* 34 */
false,
/* 35 */
false,
/* 36 */
false,
/* 37 */
false,
/* 38 */
false,
/* 39 */
false,
/* 40 */
false,
/* 41 */,
/* 42 */
false,
/* 43 */
false,
/* 44 */
false,
/* 45 */
false,
/* 46 */
false,
/* 47 */
false,
/* 48 */
false,
/* 49 */
false,
/* 50 */
false,
/* 51 */
false,
/* 52 */,
/* 53 */
false,
/* 54 */,
/* 55 */,
/* 56 */
false,
/* 57 */
false,
/* 58 */
false,
/* 59 */
false,
/* 60 */
false,
/* 61 */
false,
/* 62 */
false,
/* 63 */
false,
/* 64 */
false,
/* 65 */
false,
/* 66 */
false,
/* 67 */
false,
/* 68 */
false,
/* 69 */
false,
/* 70 */
false,
/* 71 */
false,
/* 72 */
false,
/* 73 */
false,
/* 74 */
false,
/* 75 */
false,
/* 76 */
false,
/* 77 */
false,
/* 78 */
false,
/* 79 */,
/* 80 */,
/* 81 */,
/* 82 */,
/* 83 */,
/* 84 */
false,
/* 85 */
false,
/* 86 */
false,
/* 87 */
false,
/* 88 */
false,
/* 89 */
false,
/* 90 */
false,
/* 91 */
false,
/* 92 */
false,
/* 93 */
false,
/* 94 */
false,
/* 95 */
false,
/* 96 */
false,
/* 97 */
false,
/* 98 */
false,
/* 99 */
false,
/* 100 */
false,
/* 101 */
false,
/* 102 */
false,
/* 103 */
false,
/* 104 */
false,
/* 105 */
false,
/* 106 */
false,
/* 107 */
false,
/* 108 */
false,
/* 109 */
false,
/* 110 */
false,
/* 111 */
false,
/* 112 */
false,
/* 113 */
false,
/* 114 */
false,
/* 115 */
false,
/* 116 */,
/* 117 */,
/* 118 */,
/* 119 */,
/* 120 */,
/* 121 */,
/* 122 */,
/* 123 */,
/* 124 */,
/* 125 */,
/* 126 */,
/* 127 */,
/* 128 */,
/* 129 */,
/* 130 */,
/* 131 */,
/* 132 */,
/* 133 */,
/* 134 */,
/* 135 */,
/* 136 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
    value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _react = __webpack_require__(1);

var _react2 = _interopRequireDefault(_react);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Tasks = function (_React$Component) {
    _inherits(Tasks, _React$Component);

    function Tasks(props) {
        _classCallCheck(this, Tasks);

        return _possibleConstructorReturn(this, (Tasks.__proto__ || Object.getPrototypeOf(Tasks)).call(this, props));
    }

    _createClass(Tasks, [{
        key: 'render',
        value: function render() {

            var tasks = this.props.tasks.map(function (task) {
                return _react2.default.createElement(
                    'li',
                    { key: task.id },
                    task.name
                );
            });

            return _react2.default.createElement(
                'div',
                null,
                _react2.default.createElement(
                    'h2',
                    null,
                    'Hello from tasks!'
                ),
                _react2.default.createElement(
                    'ul',
                    null,
                    tasks
                )
            );
        }
    }]);

    return Tasks;
}(_react2.default.Component);

exports.default = Tasks;

/***/ }),
/* 137 */
false,
/* 138 */
false,
/* 139 */
false,
/* 140 */
false,
/* 141 */
false,
/* 142 */
false,
/* 143 */
false,
/* 144 */
false,
/* 145 */
false,
/* 146 */
false,
/* 147 */
false,
/* 148 */
false,
/* 149 */
false,
/* 150 */
false,
/* 151 */
false,
/* 152 */
false,
/* 153 */
false,
/* 154 */
false,
/* 155 */
false,
/* 156 */
false,
/* 157 */
false,
/* 158 */
false,
/* 159 */
false,
/* 160 */
false,
/* 161 */
false,
/* 162 */
false,
/* 163 */
false,
/* 164 */
false,
/* 165 */
false,
/* 166 */
false,
/* 167 */
false,
/* 168 */
false,
/* 169 */
false,
/* 170 */
false,
/* 171 */
false,
/* 172 */
false,
/* 173 */
false,
/* 174 */
false,
/* 175 */
false,
/* 176 */
false,
/* 177 */
false,
/* 178 */
false,
/* 179 */
false,
/* 180 */
false,
/* 181 */
false,
/* 182 */
false,
/* 183 */
false,
/* 184 */
false,
/* 185 */
false,
/* 186 */
false,
/* 187 */
false,
/* 188 */
false,
/* 189 */
false,
/* 190 */
false,
/* 191 */
false,
/* 192 */
false,
/* 193 */
false,
/* 194 */
false,
/* 195 */
false,
/* 196 */
false,
/* 197 */
false,
/* 198 */
false,
/* 199 */
false,
/* 200 */
false,
/* 201 */
false,
/* 202 */
false,
/* 203 */
false,
/* 204 */
false,
/* 205 */
false,
/* 206 */
false,
/* 207 */
false,
/* 208 */
false,
/* 209 */
false,
/* 210 */
false,
/* 211 */
false,
/* 212 */
false,
/* 213 */
false,
/* 214 */
false,
/* 215 */
false,
/* 216 */
false,
/* 217 */
false,
/* 218 */
false,
/* 219 */
false,
/* 220 */
false,
/* 221 */
false,
/* 222 */
false,
/* 223 */
false,
/* 224 */
false,
/* 225 */
false,
/* 226 */
false,
/* 227 */
false,
/* 228 */
false,
/* 229 */
false,
/* 230 */
false,
/* 231 */
false,
/* 232 */
false,
/* 233 */
false,
/* 234 */
false,
/* 235 */
false,
/* 236 */
false,
/* 237 */
false,
/* 238 */
false,
/* 239 */
false,
/* 240 */
false,
/* 241 */
false,
/* 242 */
false,
/* 243 */
false,
/* 244 */
false,
/* 245 */
false,
/* 246 */
false,
/* 247 */
false,
/* 248 */
false,
/* 249 */
false,
/* 250 */
false,
/* 251 */
false,
/* 252 */
false,
/* 253 */
false,
/* 254 */
false,
/* 255 */
false,
/* 256 */
false,
/* 257 */
false,
/* 258 */
false,
/* 259 */
false,
/* 260 */
false,
/* 261 */
false,
/* 262 */
false,
/* 263 */
false,
/* 264 */
false,
/* 265 */
false,
/* 266 */
false,
/* 267 */
false,
/* 268 */
false,
/* 269 */
false,
/* 270 */
false,
/* 271 */
false,
/* 272 */
false
])