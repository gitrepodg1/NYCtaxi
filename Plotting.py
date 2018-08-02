#v1: 31/7/17: DG: Helper functions for plotting graphs

import plotly
import plotly.graph_objs as go
import qagDate
import plotly.offline
#import plotly.offline as po
import os
import uuid
import webbrowser
from plotly import optional_imports, tools, utils
from pkg_resources import resource_string
from requests.compat import json as _json
#from plotly.offline import get_plotlyjs as pjs
#from plotly.offline import get_plotlyjs as pjs

#import sys
#if sys.platform[:3] == "win":
#if sys.platform == 'darwin':
webbrowser.register('mychrome', None, webbrowser.MacOSXOSAScript('Google Chrome'), -1)   #this registers the Chrome browser


class PlotTool():
   def __init__(self,**kwargs):
       pass


class qagPlot():
 #  def __init__(self,**kwargs):
 #      self.data=[]
 #      self.layout=go.Layout()
 #      self.config=None
 #      self.use_iplot=True
 #      self.auto_update=True

   def __init__(self,target='iplot',auto_update=True,filename='plotlyTest1.html', include_plotlyjs=True, output_type='file', auto_open=True, show_link=False, **kwargs):
       self.dict={}
      # self.dict['data']=[]
       self.dict['data']={}
       self.dict['layout']=go.Layout()
       self.dict['config']={'displayModeBar': True}
       self.dict['params']={'filename':filename, 'include_plotlyjs':include_plotlyjs, 'output_type':output_type, 'auto_open':auto_open, 'show_link':show_link}
       self.dict['target']=target
       self.dict['auto_update']=auto_update
       self.dict.update(kwargs)
       #config={"displayModeBar": False}


#   def addData(self,**kwargs):
#       self.dict['data'].append(go.Scatter(kwargs))
#       if self.dict['auto_update']:
#           self.plot()

#   def removeData(self,index):
#       if index<len(self.dict['data']):
#          del self.dict['data'][index]
#          if self.dict['auto_update']:
#              self.plot()

   def addData(self,id,**kwargs):
       self.dict['data'].update({id:kwargs})
       if self.dict['auto_update']:
           self.plot()

   def removeData(self,item):
       if item in self.dict['data']:
          del self.dict['data'][item]
          if self.dict['auto_update']:
              self.plot()        


   def addConfig(self,**kwargs):
       self.dict['config'].update(kwargs)
       if self.dict['auto_update']:
           self.plot()

   def removeConfig(self,item):
       if item in self.dict['config']:
          del self.dict['config'][item]
          if self.dict['auto_update']:
              self.plot()        

   def addParams(self,**kwargs):
       self.dict['params'].update(kwargs)
       if self.dict['auto_update']:
           self.plot()

   def removeParams(self,item):
       if item in self.dict['params']:
          del self.dict['params'][item]
          if self.dict['auto_update']:
              self.plot()        

   def addLayout(self,**kwargs):
       self.dict['layout'].update(kwargs)
       if self.dict['auto_update']:
           self.plot()

   def removeLayout(self,item):
       if item in self.dict['layout']:
          del self.dict['layout'][item]
          if self.dict['auto_update']:
              self.plot()        
 



   def plot(self):
      #fig = go.Figure(data=self.data, layout=self.layout)
      dataList=[]
      for key, value in self.dict['data'].items():
          dataList.append(value)
      #print("dataList:",dataList)
      #fig = go.Figure(data=self.dict['data'], layout=self.dict['layout'])
      fig = go.Figure(data=dataList, layout=self.dict['layout'])
      if self.dict['target']=='iplot':
          paramsTmp={}                                      #need to remove the three parameters below as iplot does not use them and throws an error
          for key, value in self.dict['params'].items():
              if (key != 'include_plotlyjs') and (key != 'output_type') and (key != 'auto_open'):
                  paramsTmp[key]=value
          url1 = plotly.offline.iplot(fig, config=self.dict['config'],**paramsTmp)    #**self.dict['params']) #, filename=filename, show_link=show_link)
      else:
          #url1 = plotly.offline.plot(fig, filename=filename, include_plotlyjs=include_plotlyjs, output_type=output_type, auto_open=auto_open, show_link=show_link)
          #url1 = plotly.offline.plot(fig, config=self.dict['config'],**self.dict['params'])
          url1 = bplot(fig, config=self.dict['config'],**self.dict['params'])
   
      return url1


   def help(self):
        help_string = """
         PlotLy help can be obtained here:  https://plot.ly/python/reference/
       """
        print(help_string)
        return help_string


def get_plotlyjs():
    path = os.path.join('package_data', 'plotly.min.js')
    plotlyjs = resource_string('plotly', path).decode('utf-8')
    return plotlyjs


def bplot(figure_or_data, show_link=True, link_text='Export to plot.ly',
         validate=True, output_type='file', include_plotlyjs=True,
         filename='temp-plot.html', auto_open=True, image=None,
         image_filename='plot_image', image_width=800, image_height=600,
         config=None):
    """ Create a plotly graph locally as an HTML document or string.

    Example:
    ```
    from plotly.offline import plot
    import plotly.graph_objs as go

    plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='my-graph.html')
    # We can also download an image of the plot by setting the image parameter
    # to the image format we want
    plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='my-graph.html'
         image='jpeg')
    ```
    More examples below.

    figure_or_data -- a plotly.graph_objs.Figure or plotly.graph_objs.Data or
                      dict or list that describes a Plotly graph.
                      See https://plot.ly/python/ for examples of
                      graph descriptions.

    Keyword arguments:
    show_link (default=True) -- display a link in the bottom-right corner of
        of the chart that will export the chart to Plotly Cloud or
        Plotly Enterprise
    link_text (default='Export to plot.ly') -- the text of export link
    validate (default=True) -- validate that all of the keys in the figure
        are valid? omit if your version of plotly.js has become outdated
        with your version of graph_reference.json or if you need to include
        extra, unnecessary keys in your figure.
    output_type ('file' | 'div' - default 'file') -- if 'file', then
        the graph is saved as a standalone HTML file and `plot`
        returns None.
        If 'div', then `plot` returns a string that just contains the
        HTML <div> that contains the graph and the script to generate the
        graph.
        Use 'file' if you want to save and view a single graph at a time
        in a standalone HTML file.
        Use 'div' if you are embedding these graphs in an HTML file with
        other graphs or HTML markup, like a HTML report or an website.
    include_plotlyjs (default=True) -- If True, include the plotly.js
        source code in the output file or string.
        Set as False if your HTML file already contains a copy of the plotly.js
        library.
    filename (default='temp-plot.html') -- The local filename to save the
        outputted chart to. If the filename already exists, it will be
        overwritten. This argument only applies if `output_type` is 'file'.
    auto_open (default=True) -- If True, open the saved file in a
        web browser after saving.
        This argument only applies if `output_type` is 'file'.
    image (default=None |'png' |'jpeg' |'svg' |'webp') -- This parameter sets
        the format of the image to be downloaded, if we choose to download an
        image. This parameter has a default value of None indicating that no
        image should be downloaded. Please note: for higher resolution images
        and more export options, consider making requests to our image servers.
        Type: `help(py.image)` for more details.
    image_filename (default='plot_image') -- Sets the name of the file your
        image will be saved to. The extension should not be included.
    image_height (default=600) -- Specifies the height of the image in `px`.
    image_width (default=800) -- Specifies the width of the image in `px`.
    config (default=None) -- Plot view options dictionary. Keyword arguments
        `show_link` and `link_text` set the associated options in this
        dictionary if it doesn't contain them already.
    """
    if output_type not in ['div', 'file']:
        raise ValueError(
            "`output_type` argument must be 'div' or 'file'. "
            "You supplied `" + output_type + "``")
    if not filename.endswith('.html') and output_type == 'file':
        warnings.warn(
            "Your filename `" + filename + "` didn't end with .html. "
            "Adding .html to the end of your file.")
        filename += '.html'

    config = dict(config) if config else {}
    config.setdefault('showLink', show_link)
    config.setdefault('linkText', link_text)

    #plot_html, plotdivid, width, height = _plot_html( 
    #plot_html, plotdivid, width, height = plotly.offline._plot_html(    #DG modified
    plot_html, plotdivid, width, height = _plot_html(
        figure_or_data, config, validate,
        '100%', '100%', global_requirejs=False)

    resize_script = ''
    if width == '100%' or height == '100%':
        resize_script = (
            ''
            '<script type="text/javascript">'
            'window.addEventListener("resize", function(){{'
            'Plotly.Plots.resize(document.getElementById("{id}"));}});'
            '</script>'
        ).format(id=plotdivid)

    if output_type == 'file':
        with open(filename, 'w') as f:
            if include_plotlyjs:
                plotly_js_script = ''.join([
                    '<script type="text/javascript">',
                      get_plotlyjs(),  #pjs(),   #plotly.offline.get_plotlyjs(),    #DG modified
                    '</script>',
                ])
            else:
                plotly_js_script = ''

            if image:
                if image not in __IMAGE_FORMATS:
                    raise ValueError('The image parameter must be one of the '
                                     'following: {}'.format(__IMAGE_FORMATS)
                                     )
                # if the check passes then download script is injected.
                # write the download script:
                script = get_image_download_script('plot')
                script = script.format(format=image,
                                       width=image_width,
                                       height=image_height,
                                       filename=image_filename,
                                       plot_id=plotdivid)
            else:
                script = ''

            f.write(''.join([
                '<html>',
                '<head><meta charset="utf-8" /></head>',
                '<body>',
                plotly_js_script,
                plot_html,
                resize_script,
                script,
                '</body>',
                '</html>']))

        url = 'file://' + os.path.abspath(filename)
        if auto_open:
            #webbrowser.open(url)   #DG modified  http://www.codevoila.com/post/45/open-web-browser-window-or-new-tab-with-python
            #webbrowser.get(using='/Applications/Google Chrome.app').open(url,new=new)
            #webbrowser.get('mychrome').open_new_tab(url)
            webbrowser.get('mychrome').open(url)

# Linux
# chrome_cmd = "/usr/bin/google-chrome %s"

# Windows
# chrome_cmd = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"

# Mac
#chrome_cmd = "open -a /Applications/Google\ Chrome.app %s"

#webbrowser.get(chrome_cmd).open_new_tab(a_website)

        return url

    elif output_type == 'div':
        if include_plotlyjs:
            return ''.join([
                '<div>',
                '<script type="text/javascript">',
                get_plotlyjs(),   #pjs(),  #plotly.offline..get_plotlyjs(),    #DG modified    get_plotlyjs(),
                '</script>',
                plot_html,
                resize_script,
                '</div>',
            ])
        else:
            return plot_html

def _plot_html(figure_or_data, config, validate, default_width,
               default_height, global_requirejs):
    # force no validation if frames is in the call
    # TODO - add validation for frames in call - #605
    if 'frames' in figure_or_data:
        figure = tools.return_figure_from_figure_or_data(
            figure_or_data, False
        )
    else:
        figure = tools.return_figure_from_figure_or_data(
            figure_or_data, validate
        )

    width = figure.get('layout', {}).get('width', default_width)
    height = figure.get('layout', {}).get('height', default_height)

    try:
        float(width)
    except (ValueError, TypeError):
        pass
    else:
        width = str(width) + 'px'

    try:
        float(height)
    except (ValueError, TypeError):
        pass
    else:
        height = str(height) + 'px'

    plotdivid = uuid.uuid4()
    jdata = _json.dumps(figure.get('data', []), cls=utils.PlotlyJSONEncoder)
    jlayout = _json.dumps(figure.get('layout', {}),
                          cls=utils.PlotlyJSONEncoder)
    if 'frames' in figure_or_data:
        jframes = _json.dumps(figure.get('frames', {}),
                              cls=utils.PlotlyJSONEncoder)

    configkeys = (
        'editable',
        'autosizable',
        'fillFrame',
        'frameMargins',
        'scrollZoom',
        'doubleClick',
        'showTips',
        'showLink',
        'sendData',
        'linkText',
        'showSources',
        'displayModeBar',
        'modeBarButtonsToRemove',
        'modeBarButtonsToAdd',
        'modeBarButtons',
        'displaylogo',
        'plotGlPixelRatio',
        'setBackground',
        'topojsonURL'
    )

    config_clean = dict((k, config[k]) for k in configkeys if k in config)
    jconfig = _json.dumps(config_clean)

    # TODO: The get_config 'source of truth' should
    # really be somewhere other than plotly.plotly
    plotly_platform_url = plotly.plotly.get_config().get('plotly_domain',
                                                         'https://plot.ly')
    if (plotly_platform_url != 'https://plot.ly' and
            config['linkText'] == 'Export to plot.ly'):

        link_domain = plotly_platform_url\
            .replace('https://', '')\
            .replace('http://', '')
        link_text = config['linkText'].replace('plot.ly', link_domain)
        config['linkText'] = link_text
        jconfig = jconfig.replace('Export to plot.ly', link_text)

    if 'frames' in figure_or_data:
        script = '''
        Plotly.plot(
            '{id}',
            {data},
            {layout},
            {config}
        ).then(function () {add_frames}).then(function(){animate})
        '''.format(
            id=plotdivid,
            data=jdata,
            layout=jlayout,
            config=jconfig,
            add_frames="{" + "return Plotly.addFrames('{id}',{frames}".format(
                id=plotdivid, frames=jframes
            ) + ");}",
            animate="{" + "Plotly.animate('{id}');".format(id=plotdivid) + "}"
        )
    else:
        script = 'Plotly.newPlot("{id}", {data}, {layout}, {config})'.format(
            id=plotdivid,
            data=jdata,
            layout=jlayout,
            config=jconfig)

    optional_line1 = ('require(["plotly"], function(Plotly) {{ '
                      if global_requirejs else '')
    optional_line2 = ('}});' if global_requirejs else '')

    plotly_html_div = (
        ''
        '<div id="{id}" style="height: {height}; width: {width};" '
        'class="plotly-graph-div">'
        '</div>'
        '<script type="text/javascript">' +
        optional_line1 +
        'window.PLOTLYENV=window.PLOTLYENV || {{}};'
        'window.PLOTLYENV.BASE_URL="' + plotly_platform_url + '";'
        '{script}' +
        optional_line2 +
        '</script>'
        '').format(
        id=plotdivid, script=script,
        height=height, width=width)

    return plotly_html_div, plotdivid, width, height



def PlotlyInNotebook():
   return plotly.offline.init_notebook_mode(connected=True)

def PlotlyPlot(data,layout=None,filename=None, include_plotlyjs=True, output_type='file', auto_open=True, show_link=False, use_iplot=False):

#output_type='div' or 'file'
#image=None, image_filename='plot_image', image_width=800, image_height=600
#image = 'jpeg'

#https://plot.ly/python/configuration-options/

   """
 Keyword arguments:
    show_link (default=True) -- display a link in the bottom-right corner of
        of the chart that will export the chart to Plotly Cloud or
        Plotly Enterprise
    link_text (default='Export to plot.ly') -- the text of export link
    validate (default=True) -- validate that all of the keys in the figure
        are valid? omit if your version of plotly.js has become outdated
        with your version of graph_reference.json or if you need to include
        extra, unnecessary keys in your figure.
    output_type ('file' | 'div' - default 'file') -- if 'file', then
        the graph is saved as a standalone HTML file and `plot`
        returns None.
        If 'div', then `plot` returns a string that just contains the
        HTML <div> that contains the graph and the script to generate the
        graph.
        Use 'file' if you want to save and view a single graph at a time
        in a standalone HTML file.
        Use 'div' if you are embedding these graphs in an HTML file with
        other graphs or HTML markup, like a HTML report or an website.
    include_plotlyjs (default=True) -- If True, include the plotly.js
        source code in the output file or string.
        Set as False if your HTML file already contains a copy of the plotly.js
        library.
    filename (default='temp-plot.html') -- The local filename to save the
        outputted chart to. If the filename already exists, it will be
        overwritten. This argument only applies if `output_type` is 'file'.
    auto_open (default=True) -- If True, open the saved file in a
        web browser after saving.
        This argument only applies if `output_type` is 'file'.
    image (default=None |'png' |'jpeg' |'svg' |'webp') -- This parameter sets
        the format of the image to be downloaded, if we choose to download an
        image. This parameter has a default value of None indicating that no
        image should be downloaded. Please note: for higher resolution images
        and more export options, consider making requests to our image servers.
        Type: `help(py.image)` for more details.
    image_filename (default='plot_image') -- Sets the name of the file your
        image will be saved to. The extension should not be included.
    image_height (default=600) -- Specifies the height of the image in `px`.
    image_width (default=800) -- Specifies the width of the image in `px`.    
   """

#{displayModeBar: false}
#modeBarButtonsToRemove: ['sendDataToCloud','hoverCompareCartesian']
#url1 = plotly.offline.plot(fig, filename=filename,  config={"displayModeBar": False})
#layout = go.Layout(title='A Simple Plot', width=800, height=640)
#plotly.plotly.iplot( plot, plotly.graph_objs.Layout(title , xaxis = dict( title ,titlefont ), yaxis = dict( title ,titlefont)))
   print("use iplot:", use_iplot)
   if layout==None:
      fig = go.Figure(data=data)
   else:
      fig = go.Figure(data=data, layout=layout)
   if use_iplot:
       url1 = plotly.offline.iplot(fig, filename=filename, show_link=show_link)
   else:
       url1 = plotly.offline.plot(fig, filename=filename, include_plotlyjs=include_plotlyjs, output_type=output_type, auto_open=auto_open, show_link=show_link)
   
   return url1
 
 #https://plot.ly/python/getting-started/
 #plotly.offline.init_notebook_mode(connected=True)
 #plotly.offline.iplot()    #use this to generate plot for Jupyter Notebook


#py.image.save_as(fig, filename='a-simple-plot.png')      #DG: I think this only works with the payed version of plotly
#from IPython.display import Image
#Image('a-simple-plot.png')
#https://community.plot.ly/t/use-plotly-offline-to-save-chart-as-image-file/408/19    #says problem with storing when offline

#DG: using the image keyword does work. Stores file in the Download directory.


def Plot2d(data,layout=None):
       pass

def PlotDataLayout(data,layout=None):

    fig = go.Figure(data=data, layout=layout)


def GraphToPlot(Y,Labels,X=None,filename='plotlyTest1.html',layout=None, include_plotlyjs=True, output_type='file', auto_open=True, show_link=False, use_iplot=False):   
    data = []
    i=0
    for y in Y:
        data.append(
            go.Scatter(
                #x = y[0],
                #x = qagDate.qagDateUtil.ConvertDateFormatList(y[0],"Excel","DateTime","%d/%m/%Y","%Y%m%d"), 
                x = qagDate.qagDateUtil.ConvertDateFormatList(y[0],"String","DateTime","%Y/%m/%d","%Y%m%d"), 
               
                y = y[1],
                mode = 'lines',
                name = Labels[i]
            )
        )
        i = i + 1

   # fig = go.Figure(data=data)
    print("filename: ",filename)
   # plt3URL = plotly.offline.plot(fig, filename=filename, auto_open=False, show_link=False)

    plt3URL = PlotlyPlot(data,layout=layout,filename=filename, include_plotlyjs=include_plotlyjs, output_type=output_type, auto_open=auto_open, show_link=show_link, use_iplot=use_iplot)

    return plt3URL
#url1 = plotly.offline.plot(fig, filename='pandas-bar-chart-layout2.html', include_plotlyjs=False, output_type='div', auto_open=False, show_link=False)





#print 'X: ', X_lda[:, 1]
#print 'X: ', X_lda

#data = [
#    go.Scatter3d(
#         z=X_lda[ y==0 , 2],
#         y=X_lda[ y==0 , 1],
#         x=X_lda[ y==0 , 0],
#         name='Estimation error',
#         marker=dict(color='rgb(0,0,0)')
#    ),
#    go.Scatter3d(
#         z=X_lda[ y==1 , 2],
#         y=X_lda[ y==1 , 1],
#         x=X_lda[ y==1 , 0],
#         name='Estimation error',
#         marker=dict(color='rgb(255,0,0)')
#    ),
#    go.Scatter3d(
#         z=X_lda[ y==2 , 2],
#         y=X_lda[ y==2 , 1],
#         x=X_lda[ y==2 , 0],
#         name='Estimation error',
#         marker=dict(color='rgb(0,255,0)')
#    )
#]

#fig = go.Figure(data=data, layout=layout)
#fig = go.Figure(data=data)

#plt3URL = plotly.offline.plot_mpl(mpl_fig, filename='plotlyFigure3.html', auto_open=False, show_link=False)
#plt3URL = plotly.offline.plot([X_lda[:, 0], X_lda[:, 1]], filename='plotlyLDA1.html', auto_open=False, show_link=False)
#plt3URL = plotly.offline.plot(fig, filename='plotlyLDA1.html', auto_open=False, show_link=False)

##boxplot
#data = [go.Box(y=iris_df.loc[iris_df["Species"]=='setosa','Sepal.Length'],name='Setosa'),
#go.Box(y=iris_df.loc[iris_df["Species"]=='versicolor','Sepal.Length'],name='Versicolor'),
#go.Box(y=iris_df.loc[iris_df["Species"]=='virginica','Sepal.Length'],name='Virginica')]

#layout = go.Layout(title='Iris Dataset - Sepal.Length Boxplot',
#yaxis=dict(title='Sepal.Length'))

#fig = go.Figure(data=data, layout=layout)
#py.iplot(fig)

def help(what="Date"):

   DateFormat="""
%a - abbreviated weekday name.*
%A - full weekday name.*
%b - abbreviated month name.*
%B - full month name.*
%c - the locales date and time, such as %x, %X.*
%d - zero-padded day of the month as a decimal number [01,31].
%e - space-padded day of the month as a decimal number [ 1,31]; equivalent to %_d.
%H - hour (24-hour clock) as a decimal number [00,23].
%I - hour (12-hour clock) as a decimal number [01,12].
%j - day of the year as a decimal number [001,366].
%m - month as a decimal number [01,12].
%M - minute as a decimal number [00,59].
%L - milliseconds as a decimal number [000, 999].
%p - either AM or PM.*
%S - second as a decimal number [00,61].
%U - Sunday-based week of the year as a decimal number [00,53].
%w - Sunday-based weekday as a decimal number [0,6].
%W - Monday-based week of the year as a decimal number [00,53].
%x - the locales date, such as %-m/%-d/%Y.*
%X - the locales time, such as %-I:%M:%S %p.*
%y - year without century as a decimal number [00,99].
%Y - year with century as a decimal number.
%Z - time zone offset, such as -0700, -07:00, -07, or Z.
%% - a literal percent sign (%).
   """

   if what=='Date':
       print(DateFormat)
       #return DateFormat



