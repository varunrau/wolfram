<link rel="stylesheet" type='text/css' href='main.css' />
<link rel="stylesheet" type='text/css' href='query.css' />
<link rel="stylesheet" type='text/css' href='bootstrap.css' />
<script src='jquery-1.9.0.min.js'></script>
<script src='query.js'></script>
<div class='wrapper'>

    <div class='logo'>
        <img src='logo.png'></img>
        <div class='subtitle'>
            Physics Solver
        </div>
    </div>

    <div id='search-form'>
        <form method='POST' action='/query'>
            <textarea class='input-large' placeholder='Enter Slogan here...' name="value" type="text-area"> </textarea>
            <input class='submit-button btn' type="submit" text="solve" />
        </form>
    </div>

    %if values:
        <div class='table-wrapper'>
            <div class='output'>
                <table class='table table-bordered'>
                    <caption>Your problem has been solved!</caption>
                    <thead>
                        <th></th>
                        <th>Field</th>
                        <th>Value</th>
                    </thead>
                    <tbody>
                        %for value in values:
                            <tr class='row'>
                                <td>
                                    {{value}}
                                </td>
                                <td>
                                    {{values[value]}}
                                </td>
                            </tr>
                        %end
                </table>
                    <table class='table table-bordered'>
                    <caption style="padding: 10px;">Here are the steps used to solve the problem.</caption>
                    <thead>
                        <th></th>
                        <th>Steps</th>
                    </thead>
                    <tbody>
                        %for step in steps:
                            <tr class='row'>
                                <td>
                                    {{step}}
                                </td>
                            </tr>
                        %end
                </table>

            </div>
        </div>
    %end
</div>

