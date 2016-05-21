#!/usr/bin/env python


__author__ = "Paden Clayton <sales@fasttracksites.com>"
__version__ = "07.01.15"
__date__ = "Date: 01/15/07"
__copyright__ = "Copyright (c) 2007 Paden Clayton"
__license__ = "FTSPL"

import sys
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import cPickle
except:
	print "cpickle not found"
	sys.exit(1)
try:
	import gtk
  	import gtk.glade
  	import gobject
  	import shelve
  	import os
  	import datetime
  	import xmlrpclib
  	import imp
  	from xml.dom import minidom
except:
	sys.exit(1)

FILE_EXT = "pwi"
settingsFile = "settings.xml"

MAIN_TAG = 0
ITEM_TAG = 1
ITEM_PICTURE_TAG = 2
ITEM_NAME_TAG = 3
ITEM_SERIAL_TAG = 4
ITEM_DESCRIPTION_TAG = 5
ITEM_TYPE_TAG = 6
ITEM_QUANITY_TAG = 7
SETTINGS_TAG = 8
TYPES_TAG = 9
TYPE_NAME_TAG = 10

class pyItem:
	_xml_tags = {
		MAIN_TAG : "pyItem"
		, ITEM_TAG : "Item"
		, ITEM_PICTURE_TAG : "ItemPicture"
		, ITEM_NAME_TAG : "ItemName"
		, ITEM_SERIAL_TAG : "ItemSerial"
		, ITEM_DESCRIPTION_TAG : "ItemDescription"
		, ITEM_TYPE_TAG : "ItemType"
		, ITEM_QUANITY_TAG : "ItemQuanity"
		, SETTINGS_TAG : "Settings"
		, TYPES_TAG : "Types"
		, TYPE_NAME_TAG : "TypeName"
	}

	def __init__(self):

		#print "Script dir: ", os.path.realpath(os.path.dirname(sys.argv[0]))
		# Set the project file
		self.project_file = ""

		#Set the Glade file
		self.gladefile = "inventory-manager.glade"
		self.wTree = gtk.glade.XML(self.gladefile, "mainWindow")

		#Create our dictionay and connect it
		dic = {"on_mainWindow_destroy" : self.on_Quit
				, "on_EditSettings" : self.on_EditSettings
				, "on_AddItem" : self.on_AddItem
				, "on_DelItem" : self.on_DelItem
				, "on_About" : self.on_About
				, "on_EditItem" : self.on_EditItem
				, "on_file_open" : self.on_file_open
				, "on_file_save" : self.on_file_save}
		self.wTree.signal_autoconnect(dic)

		#Here are some variables that can be reused later
		self.cItemObject = 0
		self.cItem = 1
		self.cSerial = 2
		self.cDescription = 3
		self.cType = 4
		self.cQuanity = 5

		self.sItem = "Item Name"
		self.sSerial = "Serial Number"
		self.sDescription = "Description"
		self.sType = "Type"
		self.sQuanity = "Quanity"

		#Get the treeView from the widget Tree
		self.itemView = self.wTree.get_widget("itemView")
		#Add all of the List Columns to the itemView
		self.AddItemListColumn(self.sItem, self.cItem)
		self.AddItemListColumn(self.sSerial, self.cSerial)
		self.AddItemListColumn(self.sDescription, self.cDescription)
		self.AddItemListColumn(self.sType, self.cType)
		self.AddItemListColumn(self.sQuanity, self.cQuanity)

		#Create the listStore Model to use with the itemView
		self.itemList = gtk.ListStore(gobject.TYPE_PYOBJECT
									, gobject.TYPE_STRING
									, gobject.TYPE_STRING
									, gobject.TYPE_STRING
									, gobject.TYPE_STRING
									, gobject.TYPE_STRING)
		#Attache the model to the treeView
		self.itemView.set_model(self.itemList)

	""" Regular Functions
	-------------------------------------------------------------------------------------------------"""
	def AddItemListColumn(self, title, columnId):
		"""This function adds a column to the list view.
		First it create the gtk.TreeViewColumn and then set
		some needed properties"""

		column = gtk.TreeViewColumn(title, gtk.CellRendererText()
			, text=columnId)
		column.set_resizable(True)
		column.set_sort_column_id(columnId)
		self.itemView.append_column(column)

	def on_Quit(self, widget):
		"""Called when the application is going to quit"""
		gtk.main_quit()

	def on_EditItem(self, widget):
		"""Called when the user wants to edit an item entry"""

		# Get the selection in the gtk.TreeView
		selection = self.itemView.get_selection()
		# Get the selection iter
		model, selection_iter = selection.get_selected()

		if (selection_iter):
			"""There is a selection, so now get the the value at column
			self.cItemObject, the Item Object"""
			item = self.itemList.get_value(selection_iter, self.cItemObject)
			# Create the item dialog, based off of the current selection
			itemDlg = itemDialog(item);
			result,newItem = itemDlg.run()

			if (result == gtk.RESPONSE_OK):
				"""The user clicked Ok, so let's save the changes back
				into the gtk.ListStore"""
				self.itemList.set(selection_iter
						, self.cItemObject, newItem
						, self.cItem, newItem.item
						, self.cSerial, newItem.serial
						, self.cDescription, newItem.description
						, self.cType, newItem.type
						, self.cQuanity, newItem.quanity)


	def on_AddItem(self, widget):
		"""Called when the user wants to add an item"""
		# Create the dialog, show it, and store the results
		itemDlg = itemDialog();
		result,newItem = itemDlg.run()

		if (result == gtk.RESPONSE_OK):
			"""The user clicked Ok, so let's add this
			item to the item list"""
			self.itemList.append(newItem.getList())

	def on_DelItem(self, widget):
		"""Called when the user wants to delete an item"""
		# Get the selection in the gtk.TreeView
		selection = self.itemView.get_selection()
		# Get the selection iter
		model, selection_iter = selection.get_selected()

		if (selection_iter):
			"""There is a selection, so now get the the value at column
			self.cItemObject, the Item Object"""
			item = self.itemList.get_value(selection_iter, self.cItemObject)

			"""Actually delete the item"""
			self.itemList.remove(selection_iter)

	def on_file_open(self, widget):
		"""Called when the user wants to open an item"""

		# Get the file to open
		open_file = self.file_browse(gtk.FILE_CHOOSER_ACTION_OPEN)
		if (open_file != ""):
			# We have a path, open it for reading
			try:
				db = shelve.open(open_file,"r")
				if (db):
					# We have opened the file, so empty out our gtk.TreeView
					self.itemList.clear()
					""" Since the shelve file is not gaurenteed to be in order we
					move through the file starting at iter 0 and moving our
					way up"""
					count = 0;
					while db.has_key(str(count)):
						newitem = db[str(count)]
						self.itemList.append(newitem.getList())
						count = count +1
					db.close();
					#set the project file
					root, self.project_file = os.path.split(open_file)
				else:
					self.show_error_dlg("Error opening file")
			except:
				self.show_error_dlg("Error opening file")

	def on_file_save(self, widget):
		"""Called when the user wants to save an item list"""

		# Get the File Save path
		save_file = self.file_browse(gtk.FILE_CHOOSER_ACTION_SAVE, self.project_file)
		if (save_file != ""):
			# We have a path, ensure the proper extension
			save_file, extension = os.path.splitext(save_file)
			save_file = save_file + "." + FILE_EXT
			""" Now we have the "real" file save loction create
			the shelve file, use "n" to create a new file"""
			db = shelve.open(save_file,"n")
			"""Get the first item in the gtk.ListStore, and while it is not
			None, move forwqard through the list saving each item"""
			# Get the first item in the list
			iter = self.itemList.get_iter_root()
			while (iter):
				# Get the item at the current gtk.TreeIter
				item = self.itemList.get_value(iter, self.cItemObject)
				# Use the iters position in the list as the key name
				db[self.itemList.get_string_from_iter(iter)] = item
				# Get the next iter
				iter = self.itemList.iter_next(iter)
			#close the database and write changes to disk, we are done
			db.close();
			#set the project file
			root, self.project_file = os.path.split(save_file)

	def file_browse(self, dialog_action, file_name=""):
		"""This function is used to browse for a pyItem file.
		It can be either a save or open dialog depending on
		what dialog_action is.
		The path to the file will be returned if the user
		selects one, however a blank string will be returned
		if they cancel or do not select one.
		dialog_action - The open or save mode for the dialog either
		gtk.FILE_CHOOSER_ACTION_OPEN, gtk.FILE_CHOOSER_ACTION_SAVE"""

		if (dialog_action==gtk.FILE_CHOOSER_ACTION_OPEN):
			dialog_buttons = (gtk.STOCK_CANCEL
								, gtk.RESPONSE_CANCEL
								, gtk.STOCK_OPEN
								, gtk.RESPONSE_OK)
		else:
			dialog_buttons = (gtk.STOCK_CANCEL
								, gtk.RESPONSE_CANCEL
								, gtk.STOCK_SAVE
								, gtk.RESPONSE_OK)

		file_dialog = gtk.FileChooserDialog(title="Select Project"
					, action=dialog_action
					, buttons=dialog_buttons)
		"""set the filename if we are saving"""
		if (dialog_action==gtk.FILE_CHOOSER_ACTION_SAVE):
			file_dialog.set_current_name(file_name)
		"""Create and add the pyitem filter"""
		filter = gtk.FileFilter()
		filter.set_name("pyItem database")
		filter.add_pattern("*." + FILE_EXT)
		file_dialog.add_filter(filter)
		"""Create and add the 'all files' filter"""
		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		file_dialog.add_filter(filter)

		"""Init the return value"""
		result = ""
		if file_dialog.run() == gtk.RESPONSE_OK:
			result = file_dialog.get_filename()
		file_dialog.destroy()

		return result

	""" Dialog Box Functions
	-------------------------------------------------------------------------------------------------"""
	def on_EditSettings(self, widget):
		"""Called when the user wants to edit the settings"""
		# Create the dialog, show it, and store the results
		settingsDlg = settingsDialog();
		result = settingsDlg.run()

	def on_About(self, widget):
		"""Called when the user wants to add an item"""
		# Create the dialog, show it, and store the results
		aboutDlg = aboutDialog();
		aboutDlg.run()

	def show_error_dlg(self, error_string):
		"""This Function is used to show an error dialog when
		an error occurs.
		error_string - The error string that will be displayed
		on the dialog.
		"""
		error_dlg = gtk.MessageDialog(type=gtk.MESSAGE_ERROR
					, message_format=error_string
					, buttons=gtk.BUTTONS_OK)
		error_dlg.run()
		error_dlg.destroy()

""" Dialog Boxes
-------------------------------------------------------------------------------------------------"""

class itemDialog:
	"""This class is used to show itemDlg"""

	def __init__(self, item=None):
		"""Initialize the class.
		item - a Item object"""

		#setup the glade file
		self.gladefile = "inventory-manager.glade"
		#setup the item that we will return
		if (item):
			#They have passed an item object
			self.item = item
		else:
			#Just use a blank item
			self.item = Item()

	def get_selection_iters(self):
		"""This function gets the start and end selection
		iters from the text view.  If there is no selection
		the current position of the cursor will be returned.
		Returns - start,end - gtk.TextIter objects"""

		#init
		start = None
		end = None

		#First check to see that the text buffer is valid
		if (not self.txtBuffer):
			self.show_error_dlg("Text buffer not available")
			return start,end

		#Get the selection bounds
		bounds = self.txtBuffer.get_selection_bounds();
		if (bounds):
			#If there is a selection we are done
			start,end = bounds
		else:
			#There is no selection so just get the cursor mark
			cursor_mark = self.txtBuffer.get_insert()
			"""Set start and end to be gtk.TextIter objercts at the
			position of the cursor mark"""
			start = self.txtBuffer.get_iter_at_mark(cursor_mark)
			end = self.txtBuffer.get_iter_at_mark(cursor_mark)

		return start, end

	def insert_text(self, text):
		"""This function inserts text into the text buffer
		self.txtBuffer at the current selection.  If text is
		selected it will be overwritten, otherwise it will simply be
		inserted at the cursor position
		text - The text to be inserted in the buffer
		"""

		start, end = self.get_selection_iters();

		if ((not start)or(not end)):
			self.show_error_dlg("Error inserting text")
			return;

		#Delete the selected text (start and end will be equal after)
		self.txtBuffer.delete(start,end)
		#Save a mark at the start position since after we insert
		#the text start will be invalid
		start_mark = self.txtBuffer.create_mark(None, start, True)
		#Insert, end will be set to the end insert position
		self.txtBuffer.insert(end,text)
		start = self.txtBuffer.get_iter_at_mark(start_mark)
		#select the text, use end as the first param so that
		#it will be the cursor position
		self.txtBuffer.select_range(end,start)
		#delete the start mark
		self.txtBuffer.delete_mark(start_mark)

	def populateTypes(self):
		self.enType = self.wTree.get_widget("enType")
		self.store = gtk.ListStore(gobject.TYPE_STRING)
		#Load the xml_file to a document
		try:
			xml_document = minidom.parse(settingsFile)
			if (xml_document):
				#Loop through all child nodes of the root.
				for node in xml_document.documentElement.childNodes:
					#We are looking for the types Node
					if (node.nodeName == pyItem._xml_tags[TYPES_TAG]):
						# Now loop through the post nodes children
						for item_node in node.childNodes:
							if (item_node.nodeName == pyItem._xml_tags[TYPE_NAME_TAG]):
								#Make sure it's not a blank string
								if (item_node.firstChild):
									# Add it to our list
									self.typeName = item_node.firstChild.nodeValue.strip()
									self.store.append([self.typeName])
						#Break out of the topmost for loop
						break
			self.enType.set_model(self.store)
			self.enType.set_text_column(0)
		except IOError, (errno, strerror):
			pyItem.show_error_dlg("Error loading settings file(%s): %s" % (errno, strerror))
		except:
			pyItem.show_error_dlg("Error loading settings file.")

	def get_active_text(self, combobox):
		# Get the text of the active combo item
		model = combobox.get_model()
		active = combobox.get_active()
		if active < 0:
			return None
		return model[active][0]

	def set_active_item(self, combobox, currentItem):
		# Get the text of the active combo item
		iter = 0
		for row in self.store:
			if currentItem == row[0]:
				self.enType.set_active(iter)
			iter = iter + 1


	def run(self):
		"""This function will show the itemDlg"""

		#load the dialog from the glade file
		self.wTree = gtk.glade.XML(self.gladefile, "itemDlg")
		#Get the actual dialog widget
		self.dlg = self.wTree.get_widget("itemDlg")
		#Get all of the Entry Widgets and set their text
		self.enItem = self.wTree.get_widget("enItem")
		self.enItem.set_text(self.item.item)
		self.enSerial = self.wTree.get_widget("enSerial")
		self.enSerial.set_text(self.item.serial)
		#Get the text view
		self.enDescription = self.wTree.get_widget("enDescription")
		#Get the buffer associated with the text view
		self.txtBuffer = self.enDescription.get_buffer()
		#select all of the text
		start, end = self.txtBuffer.get_bounds()
		self.txtBuffer.select_range(end,start)
		#insert over the selection i.e. replace all the text
		self.insert_text(self.item.description)
		#put the selection at the end.
		start, end = self.txtBuffer.get_bounds()
		self.txtBuffer.select_range(end,end)
		self.enType = self.wTree.get_widget("enType")
		self.populateTypes() # Populate our comboBox for our types
		if self.item.type != "":
			self.set_active_item(self.enType, self.item.type)
		self.enQuanity = self.wTree.get_widget("enQuanity")
		self.enQuanity.set_text(self.item.quanity)

		#run the dialog and store the response
		self.result = self.dlg.run()
		#get the value of the entry fields
		self.item.item = self.enItem.get_text()
		self.item.serial = self.enSerial.get_text()
		start, end = self.txtBuffer.get_bounds()
		self.item.description = self.txtBuffer.get_text(start, end)
		self.item.type = self.get_active_text(self.enType)
		self.item.quanity = self.enQuanity.get_text()

		#we are done with the dialog, destory it
		self.dlg.destroy()

		#return the result and the item
		return self.result,self.item

class settingsDialog:
	"""This class is used to show settingsDlg"""

	def __init__(self):
		"""Initialize the class."""

		#setup the glade file
		self.gladefile = "inventory-manager.glade"
		self.wTree = gtk.glade.XML(self.gladefile, "settingsDlg")

		#Create our dictionay and connect it
		dic = {"on_AddType" : self.on_AddType
				, "on_DelType" : self.on_DelType
				, "on_CloseSettingsX" : self.on_closeSettingsX
				, "on_CloseSettings" : self.on_closeSettings}
		self.wTree.signal_autoconnect(dic)

		#setup the item that we will return
		#Here are some variables that can be reused later
		self.cTypeObject = 0
		self.cType = 1

		self.sType = "Type Name"

		#Get the treeView from the widget Tree
		self.typeView = self.wTree.get_widget("typeView")
		#Add all of the List Columns to the itemView
		self.AddTypeListColumn(self.sType, self.cType)

		#Create the listStore Model to use with the itemView
		self.typeList = gtk.ListStore(gobject.TYPE_PYOBJECT
									, gobject.TYPE_STRING)
		#Attache the model to the treeView
		self.typeView.set_model(self.typeList)

	def AddTypeListColumn(self, title, columnId):
		"""This function adds a column to the list view.
		First it create the gtk.TreeViewColumn and then set
		some needed properties"""

		column = gtk.TreeViewColumn(title, gtk.CellRendererText()
			, text=columnId)
		column.set_resizable(True)
		column.set_sort_column_id(columnId)
		self.typeView.append_column(column)

	def on_AddType(self, widget):
		"""Add a type"""
		self.enNewType = self.wTree.get_widget("enNewType")
		self.NewType = self.enNewType.get_text()
		self.listVar = [self, self.NewType]
		self.typeList.append(self.listVar)
		self.NewType = self.enNewType.set_text("")

	def on_DelType(self, widget):
		"""Delete the selected type"""
		# Get the selection in the gtk.TreeView
		selection = self.typeView.get_selection()
		# Get the selection iter
		model, selection_iter = selection.get_selected()

		if (selection_iter):
			"""There is a selection, so now get the the value at column
			self.cTypeObject, the Type Object"""
			item = self.typeList.get_value(selection_iter, self.cTypeObject)

			"""Actually delete the type"""
			self.typeList.remove(selection_iter)

	def loadSettingsXML(self, xml_document):
		#Loop through all child nodes of the root.
		for node in xml_document.documentElement.childNodes:
			#We are looking for the types Node
			if (node.nodeName == pyItem._xml_tags[TYPES_TAG]):
				# Now loop through the post nodes children
				for item_node in node.childNodes:
					if (item_node.nodeName == pyItem._xml_tags[TYPE_NAME_TAG]):
						#Make sure it's not a blank string
						if (item_node.firstChild):
							# Add it to our list
							self.typeName = item_node.firstChild.nodeValue.strip()
							self.listVar = [self, self.typeName]
							self.typeList.append(self.listVar)
				#Break out of the topmost for loop
				break

	def saveSettingsXML(self, xml_file):
		"""Save the current post to xml_file
		@param xml_file - string - path to file that
		we will save the xml to.
		@returns boolean - True success. False failure
		"""
		#Init return value
		success = False

		#Get the available DOM Implementation
		impl = minidom.getDOMImplementation()
		#Create the document, with wordpy as to base node
		xml_document = impl.createDocument(None, pyItem._xml_tags[SETTINGS_TAG], None)
		#Save the Blog settings into the XML
		#First create the "settings" xml element
		Types_element = xml_document.createElement(pyItem._xml_tags[TYPES_TAG])
		"""Cycle through the list and write the items to the settings.xml file"""
		# Get the first item in the list
		iter = self.typeList.get_iter_root()
		for row in self.typeList:
			self.rowData = row[1]

			#Creates <TypeName></TypeName>
			TypeName_element = xml_document.createElement(pyItem._xml_tags[TYPE_NAME_TAG])
			#Create <TypeName>URL</TypeName>
			TypeName_element.appendChild(xml_document.createTextNode(self.rowData))
			"""Now create:
			<Types>
				<TypeName>TypeName</TypeName>
			</Types>"""
			
			Types_element.appendChild(TypeName_element)
			
		#Now add to the xml docuemnt
		xml_document.documentElement.appendChild(Types_element)
		#Now actually try to save the file
		try:
			save_file = open(xml_file, 'w')
			#write the xml document to disc
			xml_document.documentElement.writexml(save_file)
			save_file.close()
		except IOError, (errno, strerror):
			self.show_error_dlg(
				"Error saving post(%s): %s" % (errno, strerror))
		else:
			#Allright it all worked! Set the return value
			success = True

		return success

	def on_closeSettingsX(self, widget, widget2):
		self.dlg = self.wTree.get_widget("settingsDlg")
		self.saveSettingsXML(settingsFile)
		self.dlg.destroy()

	def on_closeSettings(self, widget):
		self.dlg = self.wTree.get_widget("settingsDlg")
		self.saveSettingsXML(settingsFile)
		self.dlg.destroy()
	
	def run(self):
		#Load the xml_file to a document
		try:
			xml_document = minidom.parse(settingsFile)
			if (xml_document):
				self.loadSettingsXML(xml_document)
		except IOError, (errno, strerror):
			pyItem.show_error_dlg(self, "Error loading settings file(%s): %s" % (errno, strerror))
		except:
			pyItem.show_error_dlg(self, "Error loading settings file.")

		#return the result and the item
		#return self.result


class aboutDialog:
	"""This class is used to show aboutDlg"""

	def __init__(self):
		"""Initialize the class"""

		#setup the glade file
		self.gladefile = "inventory-manager.glade"


	def run(self):
		"""This function will show the aboutDlg"""

		#load the dialog from the glade file
		self.wTree = gtk.glade.XML(self.gladefile, "aboutDlg")
		#Get the actual dialog widget
		self.dlg = self.wTree.get_widget("aboutDlg")

		#run the dialog and store the response
		self.result = self.dlg.run()

		#we are done with the dialog, destory it
		self.dlg.destroy()

		#return the result and the item
		return self.result

class Item:
	"""This class represents all the item information"""

	def __init__(self, item="", serial="", description="", type="", quanity=""):

		self.item = item
		self.serial = serial
		self.description = description
		self.type = type
		self.quanity = quanity

	def getList(self):
		"""This function returns a list made up of the
		item information.  It is used to add an item to the
		itemList easily"""
		return [self, self.item, self.serial, self.description, self.type, self.quanity]

if __name__ == "__main__":
	item = pyItem()
	gtk.main()
