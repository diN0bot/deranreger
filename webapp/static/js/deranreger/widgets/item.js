/*jslint white: false */
/*jslint nomen: false */
/*jslint plusplus: false */
/*jslint passfail: true */
/*global window, goog, ck */

goog.provide('deranreger.widgets.Item');

goog.require('goog.ui.Component');
goog.require('goog.graphics');
goog.require('goog.graphics.SolidFill');
goog.require('goog.graphics.Stroke');
goog.require('goog.dom.classes');
goog.require('goog.dom.query');
goog.require('goog.dom.appendChild');


add_minutes = function(adate, minutes) {
	minutes = 1000 * 60 * minutes;
	return new Date(adate.getTime() + minutes);
}

deranreger.widgets.Item = function(opt_domHelper,
		start_time,
		minute_pixels) {
	goog.ui.Component.call(this, opt_domHelper);

	/**
	 * The number of pixels per minute
	 * @type number
	 * @private
	 */
	this.minute_pixels_ = 2 || minute_pixels;

	/**
	 * The start time
	 * @type Date
	 * @private
	 */
	this.start_time_ = start_time || new Date();

	/**
	 * The start time
	 * @type Date
	 * @private
	 */
	this.end_time_ = add_minutes(this.start_time_, 15);

	/**
	 * The item width, based on minute pixels and times
	 * @type number
	 * @private
	 */
	this.width_ = 100; //(this.end_time_.getTime() - this.start_time_.getTime()) * this.minute_pixels_;

	/**
	 * The item height
	 * @type number
	 * @private
	 */
	this.height_ = 50;

	/**
	 * @type number
	 * @private
	 */
	this.border_width_ = 1;

	/**
	 * @type number
	 * @private
	 */
	this.border_color_ = 'blue';

	/**
	 * @type String
	 * @private
	 */
	this.name_ = 'Hi';

	/**
	 * @type boolean
	 * @private
	 */
	this.editing_ = false;

	/**
	 * The color.
	 * @type String
	 * @private
	 */
	this.color_ = '#f89406';

	/**
	 * The text color.
	 * @type String
	 * @private
	 */
	this.font_color_ = '#000000';

	/**
	 * Event handler for this object.
	 * @type goog.events.EventHandler
	 * @private
	 */
	this.eh_ = new goog.events.EventHandler(this);

	/**
	 * Keyboard handler for this object. This object is created once the
	 * component's DOM element is known.
	 *
	 * @type goog.events.KeyHandler|Null
	 * @private
	 */
	this.kh_ = null;
};
goog.inherits(deranreger.widgets.Item, goog.ui.Component);

/** @inheritDoc */
deranreger.widgets.Item.prototype.createDom = function() {
	this.decorateInternal(this.dom_.createElement('div'));
};

/** @inheritDoc */
deranreger.widgets.Item.prototype.decorateInternal = function(element) {
	goog.base(this, 'decorateInternal', element);

	var dom    = this.getDomHelper();
	var rootEl = this.getElement();

	// decorate the root element itself
	goog.dom.classes.add(rootEl, 'item');
	//rootEl.tabIndex = 0;
};

/** @inheritDoc **/
deranreger.widgets.Item.prototype.render = function (el) {
	deranreger.widgets.Item.superClass_.render.call(this, el);
	this.draw();
};

/** Draws graphics **/
deranreger.widgets.Item.prototype.draw = function () {
	var graphics;
	var rect, fill, stroke;
	var text, font_fill, font_stroke;

	if (!this.inDocument_) {
		return;
	}
	if (this.graphics) {
		this.graphics.dispose();
	}

	this.graphics = new goog.graphics.createGraphics(
			this.width_,
			this.height_
			);
	fill = new goog.graphics.SolidFill(this.color_);
	stroke = new goog.graphics.Stroke(
			this.border_width_,
		    this.border_color_
			);
	rect = this.graphics.drawRect(
				0,
				0,
				this.width_,
				this.height_,
				stroke,
				fill);

	font_fill = new goog.graphics.SolidFill(this.font_color_);
    font_stroke = null;
	font = new goog.graphics.Font("14", "Trebuchet MS");
	if (this.editing_) {
		text = goog.dom.createDom(
				goog.dom.TagName.INPUT,
				{'type': 'text', 'value': this.name_},
				'');
		goog.dom.insertSiblingAfter(text, goog.dom.getElement('sandbox'));
	} else {
		text = this.graphics.drawText(
					this.name_,
					10, 10,
					this.width_, this.height_,
					"left", "top",
					font,
					font_stroke,
					font_fill);
	}
	goog.dom.classes.set(text, "item_name");
	this.graphics.render(this.getElement());
};

/** @inheritDoc **/
deranreger.widgets.Item.prototype.enterDocument = function() {
	deranreger.widgets.Item.superClass_.enterDocument.call(this);
    this.eh_.listen(
    		this.getContentElement(),
    		goog.events.EventType.CLICK,
    		this.on_click_
    		);
};

/** @inheritDoc **/
deranreger.widgets.Item.prototype.exitDocument = function() {
	deranreger.widgets.Item.superClass_.exitDocument.call(this);
    this.eh_.unlisten(
    		this.getContentElement(),
    		goog.events.EventType.CLICK,
    		this.on_click_
    		);
};

/** @private **/
deranreger.widgets.Item.prototype.on_click_ = function(e) {
	var text;

	text = goog.dom.query('text', e.currentTarget);

	this.editing_ = !this.editing_;
	this.draw(this.getElement());
}
